"""Tests for the utils module."""

from __future__ import annotations

from datetime import timedelta
from unittest.mock import Mock, patch

import pytest

from agent_cli.core import utils


@pytest.mark.parametrize(
    ("td", "expected"),
    [
        (timedelta(seconds=5), "5 seconds ago"),
        (timedelta(minutes=5), "5 minutes ago"),
        (timedelta(hours=5), "5 hours ago"),
        (timedelta(days=5), "5 days ago"),
    ],
)
def test_format_timedelta_to_ago(td: timedelta, expected: str) -> None:
    """Test the format_timedelta_to_ago function."""
    assert utils.format_timedelta_to_ago(td) == expected


def test_get_clipboard_text() -> None:
    """Test reading from clipboard."""
    with patch("pyperclip.paste", return_value="hello world"):
        text = utils.get_clipboard_text(quiet=True)
        assert text == "hello world"


def test_get_clipboard_text_empty() -> None:
    """Test reading from an empty clipboard."""
    with patch("pyperclip.paste", return_value=""):
        text = utils.get_clipboard_text(quiet=True)
        assert text is None


def test_get_clipboard_text_empty_not_quiet() -> None:
    """Test the get_clipboard_text function when clipboard is empty and not quiet."""
    with (
        patch("pyperclip.paste", return_value=""),
        patch(
            "agent_cli.core.utils.print_with_style",
        ) as mock_print,
    ):
        text = utils.get_clipboard_text(quiet=False)
        assert text is None
        mock_print.assert_called_once_with("Clipboard is empty.", style="yellow")


def test_print_device_index() -> None:
    """Test the print_device_index function."""
    with patch("agent_cli.core.utils.console") as mock_console:
        utils.print_device_index(1, "mock_device")
        mock_console.print.assert_called_once()


def test_print_input_panel() -> None:
    """Test the print_input_panel function."""
    with patch("agent_cli.core.utils.console") as mock_console:
        utils.print_input_panel("hello")
        mock_console.print.assert_called_once()


def test_print_output_panel() -> None:
    """Test the print_output_panel function."""
    with patch("agent_cli.core.utils.console") as mock_console:
        utils.print_output_panel("hello")
        mock_console.print.assert_called_once()


def test_print_status_message() -> None:
    """Test the print_with_style function."""
    with patch("agent_cli.core.utils.console") as mock_console:
        utils.print_with_style("hello")
        mock_console.print.assert_called_once()


def test_print_error_message() -> None:
    """Test the print_error_message function."""
    with patch("agent_cli.core.utils.console") as mock_console:
        utils.print_error_message("hello", "world")
        mock_console.print.assert_called_once()


def test_print_error_message_no_suggestion() -> None:
    """Test the print_error_message function without a suggestion."""
    with patch("agent_cli.core.utils.console") as mock_console:
        utils.print_error_message("hello")
        mock_console.print.assert_called_once()


def test_interactive_stop_event() -> None:
    """Test the InteractiveStopEvent class."""
    stop_event = utils.InteractiveStopEvent()
    assert not stop_event.is_set()
    assert not stop_event.ctrl_c_pressed

    stop_event.set()
    assert stop_event.is_set()

    stop_event.clear()
    assert not stop_event.is_set()
    assert not stop_event.ctrl_c_pressed

    assert stop_event.increment_sigint_count() == 1
    assert stop_event.ctrl_c_pressed
    assert stop_event.increment_sigint_count() == 2

    stop_event.clear()
    assert not stop_event.ctrl_c_pressed


@patch("agent_cli.core.process.kill_process")
@patch("agent_cli.core.process.is_process_running")
def test_stop_or_status_or_toggle(
    mock_is_process_running: Mock,
    mock_kill_process: Mock,
) -> None:
    """Test the stop_or_status_or_toggle function."""
    # Test stop
    mock_is_process_running.return_value = True
    mock_kill_process.return_value = True
    assert utils.stop_or_status_or_toggle("test", "test", True, False, False, quiet=True)
    mock_kill_process.assert_called_with("test")

    # Test status
    mock_is_process_running.return_value = True
    with patch("agent_cli.core.process.read_pid_file", return_value=123):
        assert utils.stop_or_status_or_toggle(
            "test",
            "test",
            False,
            True,
            False,
            quiet=True,
        )

    # Test toggle on
    mock_is_process_running.return_value = False
    assert not utils.stop_or_status_or_toggle(
        "test",
        "test",
        False,
        False,
        True,
        quiet=True,
    )

    # Test toggle off
    mock_is_process_running.return_value = True
    mock_kill_process.return_value = True
    assert utils.stop_or_status_or_toggle("test", "test", False, False, True, quiet=True)
    mock_kill_process.assert_called_with("test")
