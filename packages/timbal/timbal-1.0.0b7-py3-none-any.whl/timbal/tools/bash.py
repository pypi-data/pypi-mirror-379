import asyncio
from typing import Any

import structlog

from ..core.tool import Tool

logger = structlog.get_logger("timbal.tools.bash")


class Bash(Tool):

    def __init__(self, allowed_pattern: str, **kwargs: Any):

        # TODO Validate the pattern

        async def _execute_command(command: str) -> None:
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await process.communicate()
            stdout = stdout.decode("utf-8") if stdout else ""
            stderr = stderr.decode("utf-8") if stderr else ""
            
            return {
                "stdout": stdout,
                "stderr": stderr,
                "returncode": process.returncode,
            }
        
        # ? We could customize the name / description depending on the allowed pattern
        super().__init__(
            name="bash",
            description="Execute a bash command.",
            handler=_execute_command,
            **kwargs
        )

        self.allowed_pattern = allowed_pattern
