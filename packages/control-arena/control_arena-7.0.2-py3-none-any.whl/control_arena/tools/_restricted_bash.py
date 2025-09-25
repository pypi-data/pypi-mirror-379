import re
from functools import wraps
from typing import Literal

from inspect_ai.tool import Tool, ToolResult, bash, bash_session, tool
from inspect_ai.tool._tools._execute import code_viewer
from shortuuid import uuid


def compile_regexes(
    allowed_patterns: str | list[str] | None = None,
    denied_patterns: str | list[str] | None = None,
) -> tuple[list[re.Pattern] | None, list[re.Pattern] | None]:
    """Compile the allow and deny list regexes if necessary, otherwise leave as None."""
    # Normalize patterns to lists
    if isinstance(allowed_patterns, str):
        allowed_patterns = [allowed_patterns]
    if isinstance(denied_patterns, str):
        denied_patterns = [denied_patterns]

    allowed_regexes = None
    if isinstance(allowed_patterns, list):
        allowed_regexes = [re.compile(pattern) for pattern in allowed_patterns]

    denied_regexes = None
    if isinstance(denied_patterns, list):
        denied_regexes = [re.compile(pattern) for pattern in denied_patterns]

    return allowed_regexes, denied_regexes


def check_cmd_allowed(
    cmd: str,
    allowed_patterns: list[re.Pattern] | None = None,
    denied_patterns: list[re.Pattern] | None = None,
) -> bool:
    """Filter command based on allowed and denied regex patterns.

    Args:
        cmd (str): Command to filter.
        allowed_patterns (str | list[str] | None): Regex pattern(s) for allowed commands.
        denied_patterns (str | list[str] | None): Regex pattern(s) for denied commands.

    Returns:
        bool: True if command is allowed, False otherwise.
    """
    # Check denied patterns first
    if denied_patterns:
        for pattern in denied_patterns:
            if pattern.search(cmd):
                return False

    # If allowed patterns specified, command must match at least one
    if allowed_patterns and not any(
        pattern.search(cmd) for pattern in allowed_patterns
    ):
        return False

    return True


@tool(viewer=code_viewer("bash", "cmd"), name=bash.__name__)
def restricted_bash(
    allowed_patterns: str | list[str] | None = None,
    denied_patterns: str | list[str] | None = None,
    timeout: int | None = None,
    user: str | None = None,
    sandbox: str | None = None,
) -> Tool:
    """Bash shell command execution tool with command filtering.

    Execute bash shell commands using a sandbox environment (e.g. "docker").
    Commands can be filtered using allowed and denied regex patterns.

    This is a wrapper around the standard inspect bash tool. See additional documentation here:
    https://inspect.aisi.org.uk/reference/inspect_ai.tool.html#bash

    Args:
      allowed_patterns: Regex pattern(s) for allowed commands. If provided, only commands
                       matching at least one pattern will be allowed.
      denied_patterns: Regex pattern(s) for denied commands. Commands matching
                      any of these patterns will be blocked.
      timeout: Timeout (in seconds) for command.
      user: User to execute commands as.
      sandbox: Optional sandbox environmnent name.

    Returns:
      String with command output (stdout) or command error (stderr).
    """
    allowed_regexes, denied_regexes = compile_regexes(allowed_patterns, denied_patterns)

    # Get the original bash tool
    bash_tool = bash(timeout=timeout, user=user, sandbox=sandbox)

    @wraps(bash_tool)
    async def execute(cmd: str) -> ToolResult:
        # Check denied patterns first
        if not check_cmd_allowed(cmd, allowed_regexes, denied_regexes):
            return f"Error: Command '{cmd}' is not allowed by security policy."

        # Command passed filtering, execute it
        return await bash_tool(cmd)

    return execute


@tool(viewer=code_viewer("bash", "command"), name=bash_session.__name__)
def restricted_bash_session(
    *,
    allowed_patterns: str | list[str] | None = None,
    denied_patterns: str | list[str] | None = None,
    timeout: int | None = None,
    instance: str | None = uuid(),
) -> Tool:
    """Bash shell session command execution tool.

    Execute bash shell commands in a long running session using a sandbox environment (e.g. "docker").

    By default, a separate bash process is created within the sandbox for each
    call to `bash_session()`. You can modify this behavior by passing `instance=None`
    (which will result in a single bash process for the entire sample) or use other
    `instance` values that implement another scheme).

    This is a wrapper around the standard inspect bash_session tool. See additional documentation here:
    <https://inspect.aisi.org.uk/tools-standard.html#sec-bash-session>

    Commands can be filtered using allowed
    and denied regex patterns.

    Args:
      allowed_patterns: Regex pattern(s) for allowed commands. If provided, only commands
                       matching at least one pattern will be allowed.
      denied_patterns: Regex pattern(s) for denied commands. Commands matching
                      any of these patterns will be blocked.
      timeout: Timeout (in seconds) for command.
      wait_for_output: Maximum time (in seconds) to wait for output.
      instance: Instance id (each unique instance id has its own bash process)

    Returns:
      String with output from the shell.
    """
    allowed_regexes, denied_regexes = compile_regexes(allowed_patterns, denied_patterns)

    # Get the original bash_session tool
    session_tool = bash_session(timeout=timeout, instance=instance)

    @wraps(session_tool)
    async def execute(
        action: Literal["type", "type_submit", "restart", "read", "interrupt"],
        input: str | None = None,  # noqa: A002
    ) -> ToolResult:
        # Check denied patterns first
        if input is not None and not check_cmd_allowed(
            input, allowed_regexes, denied_regexes
        ):
            return f"Error: Input '{input}' is not allowed by security policy."

        return await session_tool(action=action, input=input)

    return execute
