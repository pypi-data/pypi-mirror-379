"""
Riso PyKit Logger - Python port of logger.sh

This module provides colorful terminal logging with workflow and step tracking.
Converted from bash script to Python for better integration and usability.
"""

import os
import sys
import time
from contextlib import contextmanager


class Colors:
    """ANSI color codes matching the original shell script"""

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    CYAN = "\033[0;36m"
    PURPLE = "\033[0;35m"
    BOLD = "\033[1m"
    WHITE = "\033[0;37m"
    NC = "\033[0m"  # No Color


class TerminalLogger:
    """
    Enhanced terminal logger with workflow and step tracking, following GitHub Actions style.

    This logger provides colorful terminal output with workflow management capabilities,
    designed to be used alongside (not replace) Python's built-in logging module.
    """

    def __init__(self, debug_mode: bool = False, error_trap: bool = False):
        self.debug_mode = debug_mode or os.getenv("DEBUG_MODE", "").lower() == "true"
        self.error_trap = error_trap or os.getenv("ERROR_TRAP", "").lower() == "true"

        # Context tracking variables
        self.current_workflow: str | None = None
        self.current_step: str | None = None
        self.current_group: str | None = None
        self.workflow_start_time: float | None = None
        self.step_start_time: float | None = None

    def _get_duration(self, start_time: float | None) -> int:
        """Calculate duration in seconds"""
        if start_time is None:
            return 0
        return int(time.time() - start_time)

    def _print(self, message: str):
        """Print to stderr like the original shell script"""
        print(message, file=sys.stderr)

    # ----------------------------------------
    # Context Management Methods
    # ----------------------------------------
    def set_workflow_context(self, workflow_name: str):
        """Set the current workflow context"""
        self.current_workflow = workflow_name
        self.workflow_start_time = time.time()

    def set_step_context(self, step_name: str):
        """Set the current step context"""
        self.current_step = step_name
        self.step_start_time = time.time()

    # ----------------------------------------
    # Workflow-level Logging Methods
    # ----------------------------------------
    def workflow_start(self, workflow_name: str):
        """Start a new workflow"""
        self.set_workflow_context(workflow_name)
        self._print(f"\n{Colors.BOLD}{Colors.PURPLE}🚀 Starting workflow: {workflow_name}{Colors.NC}")

    def workflow_end(self, workflow_name: str, status: str = "success"):
        """End the current workflow"""
        duration = ""
        if self.workflow_start_time:
            duration = f" in {self._get_duration(self.workflow_start_time)}s"

        if status == "success":
            self._print(f"{Colors.BOLD}{Colors.GREEN}✅ Workflow completed: {workflow_name}{duration}{Colors.NC}")
        else:
            self._print(f"{Colors.BOLD}{Colors.RED}❌ Workflow failed: {workflow_name}{duration}{Colors.NC}")

    # ----------------------------------------
    # Step-level Logging Methods
    # ----------------------------------------
    def step_start(self, step_name: str, step_number: int, total_steps: int):
        """Start a new step"""
        self.set_step_context(step_name)
        self._print(f"\n{Colors.BOLD}{Colors.BLUE}[{step_number}/{total_steps}] {step_name}{Colors.NC}")

    def step_end(self, step_name: str, status: str = "success"):
        """End the current step"""
        if status == "success":
            self._print(f"{Colors.GREEN}✓ {step_name} completed{Colors.NC}")
        else:
            self._print(f"{Colors.RED}✗ {step_name} failed{Colors.NC}")

    def step_end_with_timing(self, step_name: str, status: str = "success"):
        """End step with timing information"""
        duration = ""
        if self.step_start_time:
            duration = f" in {self._get_duration(self.step_start_time)}s"

        if status == "success":
            self._print(f"{Colors.GREEN}✓ {step_name} completed{duration}{Colors.NC}")
        else:
            self._print(f"{Colors.RED}✗ {step_name} failed{duration}{Colors.NC}")

    # ----------------------------------------
    # Group-level Logging Methods
    # ----------------------------------------
    def group_start(self, group_title: str):
        """Start a new group"""
        self.current_group = group_title
        self._print(f"{Colors.CYAN}▶ {group_title}{Colors.NC}")

    def group_end(self, group_title: str):
        """End the current group"""
        self._print(f"{Colors.CYAN}◀ End: {group_title}{Colors.NC}")
        self.current_group = None

    @contextmanager
    def group(self, group_title: str):
        """Context manager for groups"""
        self.group_start(group_title)
        try:
            yield
        finally:
            self.group_end(group_title)

    # ----------------------------------------
    # Command-level Logging Methods
    # ----------------------------------------
    def notice(self, message: str):
        """Log a notice message"""
        self._print(f"{Colors.BLUE}💡 NOTICE: {message}{Colors.NC}")

    def debug(self, message: str):
        """Log a debug message (only if debug mode is enabled)"""
        if self.debug_mode:
            self._print(f"{Colors.PURPLE}🐛 DEBUG: {message}{Colors.NC}")

    # ----------------------------------------
    # Basic Logging Methods
    # ----------------------------------------
    def phase(self, message: str):
        """Log a phase separator"""
        message_length = len(message)
        total_width = message_length + 10  # Add padding
        separator = "=" * total_width

        self._print(f"\n{Colors.BOLD}{Colors.PURPLE}{separator}{Colors.NC}")
        self._print(f"{Colors.BOLD}{Colors.PURPLE}     {message}{Colors.NC}")
        self._print(f"{Colors.BOLD}{Colors.PURPLE}{separator}{Colors.NC}")

    def bold_message(self, message: str):
        """Display a bold message with separators"""
        message_length = len(message)
        total_width = message_length + 10  # Add padding like log_phase
        separator = "=" * total_width

        self._print(f"{Colors.GREEN}{separator}{Colors.NC}")
        self._print(f"{Colors.GREEN}{Colors.BOLD}     {message}{Colors.NC}")
        self._print(f"{Colors.GREEN}{separator}{Colors.NC}")

    def section(self, message: str):
        """Log a section message"""
        self._print(f"{Colors.CYAN}{message}{Colors.NC}")

    def subsection(self, message: str):
        """Log a subsection message"""
        self._print("")
        self._print(f"{Colors.BOLD}{Colors.CYAN}  {message}{Colors.NC}")

    def section_info(self, message: str):
        """Log section info"""
        self._print(f"{Colors.WHITE}    {message}{Colors.NC}")

    def header(self, message: str):
        """Log a header message"""
        self._print(f"\n{Colors.BOLD}{Colors.BLUE}🎯 {message}{Colors.NC}")

    def info(self, message: str):
        """Log an info message"""
        self._print(f"{Colors.CYAN}💡 {message}{Colors.NC}")

    def success(self, message: str):
        """Log a success message"""
        self._print(f"{Colors.GREEN}🎉 {message}{Colors.NC}")

    def warning(self, message: str):
        """Log a warning message"""
        self._print(f"{Colors.YELLOW}🚨 {message}{Colors.NC}")

    def error(self, message: str):
        """Log an error message"""
        self._print(f"{Colors.RED}💥 {message}{Colors.NC}")

    def step(self, step_num: int, total: int, message: str):
        """Log a step with numbering"""
        self._print(f"{Colors.BOLD}{Colors.BLUE}[{step_num}/{total}]{Colors.NC} {Colors.CYAN}{message}{Colors.NC}")

    # ----------------------------------------
    # Error Handling Methods
    # ----------------------------------------
    def handle_error(self, error_message: str, exit_code: int = 1, recovery_hint: str | None = None):
        """Handle errors with optional recovery hints"""
        self.error(error_message)
        if recovery_hint:
            self.notice(f"Recovery hint: {recovery_hint}")

        if self.current_workflow:
            self.workflow_end(self.current_workflow, "failure")

        if self.error_trap:
            sys.exit(exit_code)


# ----------------------------------------
# Global TerminalLogger Instance
# ----------------------------------------
_global_logger = TerminalLogger()


# ----------------------------------------
# Simple API Functions (like print())
# ----------------------------------------
def log_info(message: str):
    """Simple info logging function"""
    _global_logger.info(message)


def log_success(message: str):
    """Simple success logging function"""
    _global_logger.success(message)


def log_error(message: str):
    """Simple error logging function"""
    _global_logger.error(message)


def log_warning(message: str):
    """Simple warning logging function"""
    _global_logger.warning(message)


def log_debug(message: str):
    """Simple debug logging function"""
    _global_logger.debug(message)


def log_notice(message: str):
    """Simple notice logging function"""
    _global_logger.notice(message)


def log_header(message: str):
    """Simple header logging function"""
    _global_logger.header(message)


def log_section(message: str):
    """Simple section logging function"""
    _global_logger.section(message)


def log_subsection(message: str):
    """Simple subsection logging function"""
    _global_logger.subsection(message)


def log_section_info(message: str):
    """Simple section info logging function"""
    _global_logger.section_info(message)


def log_phase(message: str):
    """Simple phase logging function"""
    _global_logger.phase(message)


def display_bold_message(message: str):
    """Simple bold message display function"""
    _global_logger.bold_message(message)


def log_workflow_start(workflow_name: str):
    """Simple workflow start function"""
    _global_logger.workflow_start(workflow_name)


def log_workflow_end(workflow_name: str, status: str = "success"):
    """Simple workflow end function"""
    _global_logger.workflow_end(workflow_name, status)


def log_step_start(step_name: str, step_number: int, total_steps: int):
    """Simple step start function"""
    _global_logger.step_start(step_name, step_number, total_steps)


def log_step_end(step_name: str, status: str = "success"):
    """Simple step end function"""
    _global_logger.step_end(step_name, status)


def log_group_start(group_title: str):
    """Simple group start function"""
    _global_logger.group_start(group_title)


def log_group_end(group_title: str):
    """Simple group end function"""
    _global_logger.group_end(group_title)
