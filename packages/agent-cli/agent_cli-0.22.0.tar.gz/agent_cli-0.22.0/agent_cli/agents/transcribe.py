"""Wyoming ASR Client for streaming microphone audio to a transcription server."""

from __future__ import annotations

import asyncio
import json
import logging
import platform
import time
from contextlib import suppress
from datetime import UTC, datetime
from pathlib import Path  # noqa: TC003
from typing import TYPE_CHECKING

import pyperclip
import typer

from agent_cli import config, opts
from agent_cli.cli import app
from agent_cli.core import process
from agent_cli.core.audio import pyaudio_context, setup_devices
from agent_cli.core.utils import (
    maybe_live,
    print_command_line_args,
    print_input_panel,
    print_output_panel,
    print_with_style,
    setup_logging,
    signal_handling_context,
    stop_or_status_or_toggle,
)
from agent_cli.services import asr
from agent_cli.services.asr import (
    create_recorded_audio_transcriber,
    get_last_recording,
    load_audio_from_file,
)
from agent_cli.services.llm import process_and_update_clipboard

if TYPE_CHECKING:
    import pyaudio

LOGGER = logging.getLogger()

SYSTEM_PROMPT = """
CRITICAL: You must respond with ONLY the cleaned transcription text. Do NOT add any prefixes, explanations, or commentary whatsoever.

WRONG responses (DO NOT DO THIS):
- "Sure. Here's the cleaned-up text: [text]"
- "Here is the cleaned text: [text]"
- "Certainly. Here's the cleaned-up text: [text]"
- Any text wrapped in quotes like "[text]"

CORRECT response: Just the cleaned text directly, nothing else.

You are an AI transcription cleanup assistant. Your purpose is to improve and refine raw speech-to-text transcriptions by correcting errors, adding proper punctuation, and enhancing readability while preserving the original meaning and intent.

Your tasks include:
- Correcting obvious speech recognition errors and mishearing
- Adding appropriate punctuation (periods, commas, question marks, etc.)
- Fixing capitalization where needed
- Removing filler words, false starts, and repeated words when they clearly weren't intentional
- Improving sentence structure and flow while maintaining the speaker's voice and meaning
- Formatting the text for better readability

Important rules:
- Do not change the core meaning or content of the transcription
- Do not add information that wasn't spoken
- Do not remove content unless it's clearly an error or filler
- Do not wrap your output in markdown or code blocks
"""

AGENT_INSTRUCTIONS = """
REMINDER: Respond with ONLY the cleaned text. No prefixes like "Here's the cleaned text:" or quotes around your response.

You will be given a block of raw transcribed text enclosed in <original-text> tags, and a cleanup instruction enclosed in <instruction> tags.

Your job is to process the transcribed text according to the instruction, which will typically involve:
- Correcting speech recognition errors
- Adding proper punctuation and capitalization
- Removing obvious filler words and false starts
- Improving readability while preserving meaning

Your response must be JUST the cleaned text - nothing before it, nothing after it, no quotes around it.
"""

INSTRUCTION = """
Please clean up this transcribed text by correcting any speech recognition errors, adding appropriate punctuation and capitalization, removing obvious filler words or false starts, and improving overall readability while preserving the original meaning and intent of the speaker.
"""


def log_transcription(
    log_file: Path,
    role: str,
    raw_transcript: str,
    processed_transcript: str | None = None,
    model_info: str | None = None,
) -> None:
    """Log transcription results with metadata."""
    log_entry = {
        "timestamp": datetime.now(UTC).isoformat(),
        "hostname": platform.node(),
        "role": role,
        "model": model_info,
        "raw_output": raw_transcript,
        "processed_output": processed_transcript,
    }

    # Append to log file
    with log_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")


async def _async_main(  # noqa: PLR0912, PLR0915, C901
    *,
    extra_instructions: str | None,
    provider_cfg: config.ProviderSelection,
    general_cfg: config.General,
    audio_in_cfg: config.AudioInput | None = None,
    wyoming_asr_cfg: config.WyomingASR,
    openai_asr_cfg: config.OpenAIASR,
    ollama_cfg: config.Ollama,
    openai_llm_cfg: config.OpenAILLM,
    gemini_llm_cfg: config.GeminiLLM,
    llm_enabled: bool,
    transcription_log: Path | None,
    p: pyaudio.PyAudio | None = None,
    # Optional parameters for file-based transcription
    audio_file_path: Path | None = None,
    save_recording: bool = True,
) -> None:
    """Unified async entry point for both live and file-based transcription."""
    start_time = time.monotonic()
    transcript: str | None

    with maybe_live(not general_cfg.quiet) as live:
        if audio_file_path:
            # File-based transcription
            audio_data = load_audio_from_file(audio_file_path, LOGGER)
            if not audio_data:
                print_with_style(
                    f"❌ Failed to load audio from {audio_file_path}",
                    style="red",
                )
                return

            recorded_transcriber = create_recorded_audio_transcriber(provider_cfg)

            asr_config = (
                openai_asr_cfg if provider_cfg.asr_provider == "openai" else wyoming_asr_cfg
            )
            # Call with appropriate arguments based on provider
            if provider_cfg.asr_provider == "openai":
                transcript = await recorded_transcriber(
                    audio_data,
                    asr_config,
                    LOGGER,
                    quiet=general_cfg.quiet,
                )
            else:  # Wyoming expects keyword arguments
                transcript = await recorded_transcriber(
                    audio_data=audio_data,
                    wyoming_asr_cfg=asr_config,
                    logger=LOGGER,
                    quiet=general_cfg.quiet,
                )
        else:
            # Live recording transcription
            if not audio_in_cfg or not p:
                msg = "Missing audio configuration for live recording"
                raise ValueError(msg)

            with signal_handling_context(LOGGER, general_cfg.quiet) as stop_event:
                live_transcriber = asr.create_transcriber(
                    provider_cfg,
                    audio_in_cfg,
                    wyoming_asr_cfg,
                    openai_asr_cfg,
                )
                transcript = await live_transcriber(
                    logger=LOGGER,
                    p=p,
                    stop_event=stop_event,
                    quiet=general_cfg.quiet,
                    live=live,
                    save_recording=save_recording,
                )

        elapsed = time.monotonic() - start_time

        if llm_enabled and transcript:
            if not general_cfg.quiet:
                print_input_panel(
                    transcript,
                    title="📝 Raw Transcript",
                    subtitle=f"[dim]took {elapsed:.2f}s[/dim]",
                )
            if general_cfg.clipboard:
                pyperclip.copy(transcript)
                LOGGER.info("Copied raw transcript to clipboard before LLM processing.")
            instructions = AGENT_INSTRUCTIONS
            if extra_instructions:
                instructions += f"\n\n{extra_instructions}"

            # Get model info for logging
            if provider_cfg.llm_provider == "local":
                model_info = f"{provider_cfg.llm_provider}:{ollama_cfg.llm_ollama_model}"
            elif provider_cfg.llm_provider == "openai":
                model_info = f"{provider_cfg.llm_provider}:{openai_llm_cfg.llm_openai_model}"
            elif provider_cfg.llm_provider == "gemini":
                model_info = f"{provider_cfg.llm_provider}:{gemini_llm_cfg.llm_gemini_model}"
            else:
                msg = f"Unsupported LLM provider: {provider_cfg.llm_provider}"
                raise ValueError(msg)

            processed_transcript = await process_and_update_clipboard(
                system_prompt=SYSTEM_PROMPT,
                agent_instructions=instructions,
                provider_cfg=provider_cfg,
                ollama_cfg=ollama_cfg,
                openai_cfg=openai_llm_cfg,
                gemini_cfg=gemini_llm_cfg,
                logger=LOGGER,
                original_text=transcript,
                instruction=INSTRUCTION,
                clipboard=general_cfg.clipboard,
                quiet=general_cfg.quiet,
                live=live,
            )

            # Log transcription if requested
            if transcription_log:
                log_transcription(
                    log_file=transcription_log,
                    role="assistant",
                    raw_transcript=transcript,
                    processed_transcript=processed_transcript,
                    model_info=model_info,
                )
            return

    # When not using LLM, show transcript in output panel for consistency
    if transcript:
        if general_cfg.quiet:
            # Quiet mode: print result to stdout for Keyboard Maestro to capture
            print(transcript)
        else:
            print_output_panel(
                transcript,
                title="📝 Transcript",
                subtitle="[dim]Copied to clipboard[/dim]" if general_cfg.clipboard else "",
            )

        # Log transcription if requested (raw only)
        if transcription_log:
            asr_model_info = f"{provider_cfg.asr_provider}"
            if provider_cfg.asr_provider == "openai":
                asr_model_info += f":{openai_asr_cfg.asr_openai_model}"
            log_transcription(
                log_file=transcription_log,
                role="user",
                raw_transcript=transcript,
                processed_transcript=None,
                model_info=asr_model_info,
            )

        if general_cfg.clipboard:
            pyperclip.copy(transcript)
            LOGGER.info("Copied transcript to clipboard.")
        else:
            LOGGER.info("Clipboard copy disabled.")
    else:
        LOGGER.info("Transcript empty.")
        if not general_cfg.quiet:
            print_with_style("⚠️ No transcript captured.", style="yellow")


@app.command("transcribe")
def transcribe(  # noqa: PLR0912
    *,
    extra_instructions: str | None = typer.Option(
        None,
        "--extra-instructions",
        help="Additional instructions for the LLM to process the transcription.",
    ),
    from_file: Path | None = opts.FROM_FILE,
    last_recording: int = opts.LAST_RECORDING,
    save_recording: bool = opts.SAVE_RECORDING,
    # --- Provider Selection ---
    asr_provider: str = opts.ASR_PROVIDER,
    llm_provider: str = opts.LLM_PROVIDER,
    # --- ASR (Audio) Configuration ---
    input_device_index: int | None = opts.INPUT_DEVICE_INDEX,
    input_device_name: str | None = opts.INPUT_DEVICE_NAME,
    asr_wyoming_ip: str = opts.ASR_WYOMING_IP,
    asr_wyoming_port: int = opts.ASR_WYOMING_PORT,
    asr_openai_model: str = opts.ASR_OPENAI_MODEL,
    # --- LLM Configuration ---
    llm_ollama_model: str = opts.LLM_OLLAMA_MODEL,
    llm_ollama_host: str = opts.LLM_OLLAMA_HOST,
    llm_openai_model: str = opts.LLM_OPENAI_MODEL,
    openai_api_key: str | None = opts.OPENAI_API_KEY,
    openai_base_url: str | None = opts.OPENAI_BASE_URL,
    llm_gemini_model: str = opts.LLM_GEMINI_MODEL,
    gemini_api_key: str | None = opts.GEMINI_API_KEY,
    llm: bool = opts.LLM,
    # --- Process Management ---
    stop: bool = opts.STOP,
    status: bool = opts.STATUS,
    toggle: bool = opts.TOGGLE,
    # --- General Options ---
    clipboard: bool = opts.CLIPBOARD,
    log_level: str = opts.LOG_LEVEL,
    log_file: str | None = opts.LOG_FILE,
    list_devices: bool = opts.LIST_DEVICES,
    quiet: bool = opts.QUIET,
    config_file: str | None = opts.CONFIG_FILE,
    print_args: bool = opts.PRINT_ARGS,
    transcription_log: Path | None = opts.TRANSCRIPTION_LOG,
) -> None:
    """Wyoming ASR Client for streaming microphone audio to a transcription server."""
    if print_args:
        print_command_line_args(locals())
    setup_logging(log_level, log_file, quiet=quiet)

    # Expand user path for transcription log
    if transcription_log:
        transcription_log = transcription_log.expanduser()

    # Handle recovery options
    if last_recording and from_file:
        print_with_style("❌ Cannot use both --last-recording and --from-file", style="red")
        return

    # Determine audio source
    audio_file_path = None
    if last_recording > 0:  # 0 means disabled
        audio_file_path = get_last_recording(last_recording)
        if not audio_file_path:
            if last_recording == 1:
                print_with_style("❌ No saved recordings found", style="red")
            else:
                print_with_style(
                    f"❌ Recording #{last_recording} not found (not enough recordings)",
                    style="red",
                )
            return
        if not quiet:
            ordinal = "most recent" if last_recording == 1 else f"#{last_recording}"
            print_with_style(
                f"📁 Using {ordinal} recording: {audio_file_path.name}",
                style="blue",
            )
    elif from_file:
        audio_file_path = from_file.expanduser()
        if not audio_file_path.exists():
            print_with_style(f"❌ File not found: {audio_file_path}", style="red")
            return

    # Create all config objects once
    general_cfg = config.General(
        log_level=log_level,
        log_file=log_file,
        quiet=quiet,
        list_devices=list_devices,
        clipboard=clipboard,
    )
    provider_cfg = config.ProviderSelection(
        asr_provider=asr_provider,
        llm_provider=llm_provider,
        tts_provider="local",  # Not used in transcribe
    )
    wyoming_asr_cfg = config.WyomingASR(
        asr_wyoming_ip=asr_wyoming_ip,
        asr_wyoming_port=asr_wyoming_port,
    )
    openai_asr_cfg = config.OpenAIASR(
        asr_openai_model=asr_openai_model,
        openai_api_key=openai_api_key,
    )
    ollama_cfg = config.Ollama(
        llm_ollama_model=llm_ollama_model,
        llm_ollama_host=llm_ollama_host,
    )
    openai_llm_cfg = config.OpenAILLM(
        llm_openai_model=llm_openai_model,
        openai_api_key=openai_api_key,
        openai_base_url=openai_base_url,
    )
    gemini_llm_cfg = config.GeminiLLM(
        llm_gemini_model=llm_gemini_model,
        gemini_api_key=gemini_api_key,
    )

    # Handle recovery mode (transcribing from file)
    if audio_file_path:
        # We're transcribing from a saved file
        asyncio.run(
            _async_main(
                audio_file_path=audio_file_path,
                extra_instructions=extra_instructions,
                provider_cfg=provider_cfg,
                general_cfg=general_cfg,
                wyoming_asr_cfg=wyoming_asr_cfg,
                openai_asr_cfg=openai_asr_cfg,
                ollama_cfg=ollama_cfg,
                openai_llm_cfg=openai_llm_cfg,
                gemini_llm_cfg=gemini_llm_cfg,
                llm_enabled=llm,
                transcription_log=transcription_log,
            ),
        )
        return

    # Normal recording mode
    process_name = "transcribe"
    if stop_or_status_or_toggle(
        process_name,
        "transcribe",
        stop,
        status,
        toggle,
        quiet=general_cfg.quiet,
    ):
        return

    with pyaudio_context() as p:
        audio_in_cfg = config.AudioInput(
            input_device_index=input_device_index,
            input_device_name=input_device_name,
        )

        # We only use setup_devices for its input device handling
        device_info = setup_devices(p, general_cfg, audio_in_cfg, None)
        if device_info is None:
            return
        input_device_index, _, _ = device_info
        audio_in_cfg.input_device_index = input_device_index

        # Use context manager for PID file management
        with process.pid_file_context(process_name), suppress(KeyboardInterrupt):
            asyncio.run(
                _async_main(
                    extra_instructions=extra_instructions,
                    provider_cfg=provider_cfg,
                    general_cfg=general_cfg,
                    audio_in_cfg=audio_in_cfg,
                    wyoming_asr_cfg=wyoming_asr_cfg,
                    openai_asr_cfg=openai_asr_cfg,
                    ollama_cfg=ollama_cfg,
                    openai_llm_cfg=openai_llm_cfg,
                    gemini_llm_cfg=gemini_llm_cfg,
                    llm_enabled=llm,
                    transcription_log=transcription_log,
                    save_recording=save_recording,
                    p=p,
                ),
            )
