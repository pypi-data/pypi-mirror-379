"""
Riso PyKit Logging Package

A Python logging package that provides colorful terminal logging with workflow tracking.
Converted from logger.sh bash script to Python for better integration.

Usage:
    from pykit.logging import log_info, log_success, log_error, log_warning

    log_info("This is an info message")
    log_success("Operation completed successfully")
    log_error("Something went wrong")
    log_warning("This is a warning")

Or using the TerminalLogger class:
    from pykit.logging import TerminalLogger

    logger = TerminalLogger()
    logger.workflow_start("My Workflow")
    logger.step_start("Step 1", 1, 3)
    logger.info("Processing...")
    logger.step_end("Step 1", "success")
    logger.workflow_end("My Workflow", "success")
"""

from .logger import Colors
from .logger import TerminalLogger
from .logger import display_bold_message
from .logger import log_debug
from .logger import log_error
from .logger import log_group_end
from .logger import log_group_start
from .logger import log_header
from .logger import log_info
from .logger import log_notice
from .logger import log_phase
from .logger import log_section
from .logger import log_section_info
from .logger import log_step_end
from .logger import log_step_start
from .logger import log_subsection
from .logger import log_success
from .logger import log_warning
from .logger import log_workflow_end
from .logger import log_workflow_start

__version__ = "1.0.0"
__author__ = "Riso PyKit"
__all__ = [
    "Colors",
    "TerminalLogger",
    "display_bold_message",
    "log_debug",
    "log_error",
    "log_group_end",
    "log_group_start",
    "log_header",
    "log_info",
    "log_notice",
    "log_phase",
    "log_section",
    "log_section_info",
    "log_step_end",
    "log_step_start",
    "log_subsection",
    "log_success",
    "log_warning",
    "log_workflow_end",
    "log_workflow_start",
]
