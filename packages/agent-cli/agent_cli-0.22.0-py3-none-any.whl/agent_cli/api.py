"""FastAPI web service for Agent CLI transcription."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Annotated, Any

from fastapi import Depends, FastAPI, File, Form, HTTPException, Request, UploadFile
from pydantic import BaseModel

from agent_cli import config, opts
from agent_cli.agents.transcribe import AGENT_INSTRUCTIONS, INSTRUCTION, SYSTEM_PROMPT
from agent_cli.core.audio_format import VALID_EXTENSIONS, convert_audio_to_wyoming_format
from agent_cli.core.transcription_logger import get_default_logger
from agent_cli.services import asr
from agent_cli.services.llm import process_and_update_clipboard

# Configure logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

app = FastAPI(
    title="Agent CLI Transcription API",
    description="Web service for audio transcription and text cleanup",
    version="1.0.0",
)


@app.middleware("http")
async def log_requests(request: Request, call_next) -> Any:  # type: ignore[no-untyped-def]  # noqa: ANN001
    """Log basic request information."""
    client_ip = request.client.host if request.client else "unknown"
    LOGGER.info("%s %s from %s", request.method, request.url.path, client_ip)

    response = await call_next(request)

    if response.status_code >= 400:  # noqa: PLR2004
        LOGGER.warning(
            "Request failed: %s %s → %d",
            request.method,
            request.url.path,
            response.status_code,
        )

    return response


class TranscriptionResponse(BaseModel):
    """Response model for transcription endpoint."""

    raw_transcript: str
    cleaned_transcript: str | None = None
    success: bool
    error: str | None = None


class HealthResponse(BaseModel):
    """Response model for health check."""

    status: str
    version: str


class TranscriptionRequest(BaseModel):
    """Request model for transcription endpoint."""

    cleanup: bool = True
    extra_instructions: str | None = None


async def parse_transcription_form(
    cleanup: Annotated[str | bool, Form()] = True,
    extra_instructions: Annotated[str | None, Form()] = None,
) -> TranscriptionRequest:
    """Parse form data into TranscriptionRequest model."""
    cleanup_bool = cleanup.lower() in ("true", "1", "yes") if isinstance(cleanup, str) else cleanup
    return TranscriptionRequest(cleanup=cleanup_bool, extra_instructions=extra_instructions)


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy", version="1.0.0")


async def _transcribe_with_provider(
    audio_data: bytes,
    provider_cfg: config.ProviderSelection,
    wyoming_asr_cfg: config.WyomingASR,
    openai_asr_cfg: config.OpenAIASR,
) -> str:
    """Transcribe audio using the configured provider."""
    transcriber = asr.create_recorded_audio_transcriber(provider_cfg)

    if provider_cfg.asr_provider == "local":
        return await transcriber(
            audio_data=audio_data,
            wyoming_asr_cfg=wyoming_asr_cfg,
            logger=LOGGER,
        )
    if provider_cfg.asr_provider == "openai":
        return await transcriber(
            audio_data=audio_data,
            openai_asr_cfg=openai_asr_cfg,
            logger=LOGGER,
        )
    msg = f"Unsupported ASR provider: {provider_cfg.asr_provider}"
    raise ValueError(msg)


def _is_valid_audio_file(value: Any) -> bool:
    """Check if the provided value is a valid audio file."""
    return (
        hasattr(value, "filename")
        and hasattr(value, "content_type")
        and (
            (value.content_type and value.content_type.startswith("audio/"))
            or (value.filename and value.filename.lower().endswith(VALID_EXTENSIONS))
        )
    )


async def _extract_audio_file_from_request(
    request: Request,
    audio: UploadFile | None,
) -> UploadFile:
    """Extract and validate audio file from request."""
    # First try the standard 'audio' parameter
    if audio is not None:
        return audio

    # iOS Shortcuts may use a different field name, scan form for audio files
    LOGGER.info("No 'audio' parameter found, scanning form fields for audio files")
    form_data = await request.form()

    for key, value in form_data.items():
        if _is_valid_audio_file(value):
            LOGGER.info("Found audio file in field '%s': %s", key, value.filename)
            return value

    # No audio file found anywhere
    raise HTTPException(
        status_code=422,
        detail="No audio file provided. Ensure the form field is named 'audio' and type is 'File'.",
    )


def _validate_audio_file(audio: UploadFile) -> None:
    """Validate audio file and return file extension."""
    if not audio or not audio.filename:
        LOGGER.error("No filename provided in request")
        raise HTTPException(status_code=400, detail="No filename provided")

    file_ext = Path(audio.filename).suffix.lower()

    if file_ext not in VALID_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported audio format: {file_ext}. Supported: {', '.join(VALID_EXTENSIONS)}",
        )


def _load_transcription_configs() -> tuple[
    config.ProviderSelection,
    config.WyomingASR,
    config.OpenAIASR,
    config.Ollama,
    config.OpenAILLM,
    config.GeminiLLM,
    dict[str, Any],
]:
    """Load and create all required configuration objects."""
    loaded_config = config.load_config()
    wildcard_config = loaded_config.get("defaults", {})
    command_config = loaded_config.get("transcribe", {})
    defaults = {**wildcard_config, **command_config}

    provider_cfg = config.ProviderSelection(
        asr_provider=defaults.get("asr_provider", opts.ASR_PROVIDER.default),  # type: ignore[attr-defined]
        llm_provider=defaults.get("llm_provider", opts.LLM_PROVIDER.default),  # type: ignore[attr-defined]
        tts_provider=opts.TTS_PROVIDER.default,  # type: ignore[attr-defined]
    )
    wyoming_asr_cfg = config.WyomingASR(
        asr_wyoming_ip=defaults.get("asr_wyoming_ip", opts.ASR_WYOMING_IP.default),  # type: ignore[attr-defined]
        asr_wyoming_port=defaults.get("asr_wyoming_port", opts.ASR_WYOMING_PORT.default),  # type: ignore[attr-defined]
    )
    openai_asr_cfg = config.OpenAIASR(
        asr_openai_model=defaults.get("asr_openai_model", opts.ASR_OPENAI_MODEL.default),  # type: ignore[attr-defined]
        openai_api_key=defaults.get("openai_api_key", opts.OPENAI_API_KEY.default),  # type: ignore[attr-defined,union-attr]
    )
    ollama_cfg = config.Ollama(
        llm_ollama_model=defaults.get("llm_ollama_model", opts.LLM_OLLAMA_MODEL.default),  # type: ignore[attr-defined]
        llm_ollama_host=defaults.get("llm_ollama_host", opts.LLM_OLLAMA_HOST.default),  # type: ignore[attr-defined]
    )
    openai_llm_cfg = config.OpenAILLM(
        llm_openai_model=defaults.get("llm_openai_model", opts.LLM_OPENAI_MODEL.default),  # type: ignore[attr-defined]
        openai_api_key=defaults.get("openai_api_key", opts.OPENAI_API_KEY.default),  # type: ignore[attr-defined,union-attr]
        openai_base_url=defaults.get("openai_base_url", opts.OPENAI_BASE_URL.default),  # type: ignore[attr-defined,union-attr]
    )
    gemini_llm_cfg = config.GeminiLLM(
        llm_gemini_model=defaults.get("llm_gemini_model", opts.LLM_GEMINI_MODEL.default),  # type: ignore[attr-defined]
        gemini_api_key=defaults.get("gemini_api_key", opts.GEMINI_API_KEY.default),  # type: ignore[attr-defined,union-attr]
    )

    return (
        provider_cfg,
        wyoming_asr_cfg,
        openai_asr_cfg,
        ollama_cfg,
        openai_llm_cfg,
        gemini_llm_cfg,
        defaults,
    )


def _convert_audio_for_local_asr(audio_data: bytes, filename: str) -> bytes:
    """Convert audio to Wyoming format if needed for local ASR."""
    LOGGER.info("Converting %s audio to Wyoming format", filename)
    converted_data = convert_audio_to_wyoming_format(audio_data, filename)
    LOGGER.info("Audio conversion successful")
    return converted_data


async def _process_transcript_cleanup(
    raw_transcript: str,
    cleanup: bool,
    extra_instructions: str | None,
    defaults: dict[str, Any],
    provider_cfg: config.ProviderSelection,
    ollama_cfg: config.Ollama,
    openai_llm_cfg: config.OpenAILLM,
    gemini_llm_cfg: config.GeminiLLM,
) -> str | None:
    """Process transcript cleanup with LLM if requested."""
    if not cleanup:
        return None

    instructions = AGENT_INSTRUCTIONS
    config_extra = defaults.get("extra_instructions", "")
    if config_extra:
        instructions += f"\n\n{config_extra}"
    if extra_instructions:
        instructions += f"\n\n{extra_instructions}"

    return await process_and_update_clipboard(
        system_prompt=SYSTEM_PROMPT,
        agent_instructions=instructions,
        provider_cfg=provider_cfg,
        ollama_cfg=ollama_cfg,
        openai_cfg=openai_llm_cfg,
        gemini_cfg=gemini_llm_cfg,
        logger=LOGGER,
        original_text=raw_transcript,
        instruction=INSTRUCTION,
        clipboard=False,  # Don't copy to clipboard in web service
        quiet=True,
        live=None,
    )


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(
    request: Request,
    form_data: Annotated[TranscriptionRequest, Depends(parse_transcription_form)],
    audio: Annotated[UploadFile | None, File()] = None,
) -> TranscriptionResponse:
    """Transcribe audio file and optionally clean up the text.

    Args:
        request: FastAPI request object
        audio: Audio file (wav, mp3, m4a, etc.)
        form_data: Form data with cleanup and extra_instructions

    Returns:
        TranscriptionResponse with raw and cleaned transcripts

    """
    # Initialize variables outside try block to ensure they exist in finally block
    raw_transcript = ""
    cleaned_transcript = None

    try:
        # Extract and validate audio file
        audio_file = await _extract_audio_file_from_request(request, audio)
        _validate_audio_file(audio_file)

        # Extract form data (Pydantic handles string->bool conversion automatically)
        cleanup = form_data.cleanup
        extra_instructions = form_data.extra_instructions

        # Load all configurations
        (
            provider_cfg,
            wyoming_asr_cfg,
            openai_asr_cfg,
            ollama_cfg,
            openai_llm_cfg,
            gemini_llm_cfg,
            defaults,
        ) = _load_transcription_configs()

        # Save uploaded file
        audio_data = await audio_file.read()

        # Convert audio to Wyoming format if using local ASR
        if provider_cfg.asr_provider == "local":
            audio_data = _convert_audio_for_local_asr(audio_data, audio_file.filename)

        # Transcribe audio using the configured provider
        raw_transcript = await _transcribe_with_provider(
            audio_data,
            provider_cfg,
            wyoming_asr_cfg,
            openai_asr_cfg,
        )

        if not raw_transcript:
            return TranscriptionResponse(
                raw_transcript="",
                success=False,
                error="No transcript generated from audio",
            )

        # Process transcript cleanup if requested
        cleaned_transcript = await _process_transcript_cleanup(
            raw_transcript,
            cleanup,
            extra_instructions,
            defaults,
            provider_cfg,
            ollama_cfg,
            openai_llm_cfg,
            gemini_llm_cfg,
        )

        # If cleanup was requested but failed, indicate partial success
        if cleanup and cleaned_transcript is None:
            return TranscriptionResponse(
                raw_transcript=raw_transcript,
                cleaned_transcript=None,
                success=True,  # Transcription succeeded even if cleanup failed
                error="Transcription successful but cleanup failed. Check LLM configuration.",
            )

        return TranscriptionResponse(
            raw_transcript=raw_transcript,
            cleaned_transcript=cleaned_transcript,
            success=True,
        )

    except HTTPException:
        # Re-raise HTTPExceptions so FastAPI handles them properly
        raise
    except Exception as e:
        LOGGER.exception("Error during transcription")
        return TranscriptionResponse(raw_transcript="", success=False, error=str(e))
    finally:
        # Log the transcription automatically (even if it failed)
        # Only log if we have something to log
        if raw_transcript or cleaned_transcript:
            try:
                transcription_logger = get_default_logger()
                transcription_logger.log_transcription(
                    raw=raw_transcript,
                    processed=cleaned_transcript,
                )
            except Exception as log_error:
                LOGGER.warning("Failed to log transcription: %s", log_error)
