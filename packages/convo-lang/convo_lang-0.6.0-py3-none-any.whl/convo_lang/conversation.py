from __future__ import annotations
from dataclasses import dataclass, field
import json
from typing import Any, Callable, Dict, List, Optional

from .convo_cli_runner import ConvoCLIRunner
from .errors import ParseError


@dataclass
class Conversation:
    """
    Minimal in-memory builder for .convo with pluggable CLI runner.
    """
    config: Dict[str, Any] = field(default_factory=dict)
    callbacks: Dict[str, Callable[..., Any]] = field(default_factory=dict)
    convo_text: str = ""
    messages: List[Dict[str, Any]] = field(default_factory=list)
    syntax_messages: List[Dict[str, Any]] = field(default_factory=list)
    state: Dict[str, Any] = field(default_factory=dict)
    convo_cli_runner: Optional[ConvoCLIRunner] = None

    def add_convo_text(self, content: str) -> None:
        """Append raw text into the .convo source (accepts content that may start with '*convo*')."""
        if content.startswith("*convo*"):
            content = content[7:].lstrip()
        self.convo_text += content.rstrip() + "\n\n"

    def add_message(self, role: str, content: str) -> None:
        """Append a role block into the .convo source."""
        role = role.strip()
        self.convo_text += f"> {role}\n{content.rstrip()}\n\n"

    def add_user_message(self, content: str) -> None:
        self.add_message("user", content)

    def add_assistant_message(self, content: str) -> None:
        self.add_message("assistant", content)

    def add_system_message(self, content: str) -> None:
        self.add_message("system", content)

    def complete(
        self,
        *,
        variables: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = 120.0,
        working_dir: Optional[str] = None,
    ) -> str:
        """
        Run the current in-memory .convo via the injected ConvoCLIRunner.
        Returns (full_transcript, last_assistant_text).
        """
        if not self.convo_cli_runner:
            self.convo_cli_runner = ConvoCLIRunner(config=self.config)
        transcript = self.convo_cli_runner.run_text(
            self.convo_text,
            variables=variables,
            timeout=timeout,
            working_dir=working_dir,
            extra_args=["--print-state", "--print-messages", "--print-flat"],
        )
        self._parse_prefixed(transcript)
        return self._last_assistant_content()

    def _last_assistant_content(self) -> str:
        last_message = self.messages[-1]
        if last_message.get("role") == "assistant":
            return last_message.get("content", "")
        raise ParseError("No assistant message found in transcript.")

    def _parse_prefixed(self, transcript: str) -> None:
        state_lines = [l[2:] for l in transcript.splitlines()
                       if l.startswith("s:")]
        syntax_lines   = [l[2:] for l in transcript.splitlines()
                          if l.startswith("m:")]
        flat_lines  = [l[2:] for l in transcript.splitlines()
                       if l.startswith("f:")]
        result_lines  = [l[2:] if l.startswith(": ") else l[1:]
                         for l in transcript.splitlines() if l.startswith(":")]
        try:
            self.state = (json.loads("".join(state_lines))
                          if state_lines else {})
            self.syntax_messages = (json.loads("".join(syntax_lines))
                                    if syntax_lines else [])
            self.messages = (json.loads("".join(flat_lines))
                             if flat_lines else [])
        except json.JSONDecodeError as e:
            raise ParseError(
                f"Failed to parse CLI output JSON: {e}\n"
                f"Transcript:\n{transcript}"
            ) from e
        self.convo_text = "\n\n".join(result_lines).strip()

    def clear(self) -> None:
        self.convo_text = ""
        self.messages.clear()
        self.syntax_messages.clear()
        self.state.clear()

    def to_convo(self) -> str:
        return self.convo_text
