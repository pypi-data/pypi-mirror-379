"""
Test suite for pykit.logging package

Tests all functionality converted from logger.sh bash script to Python.
"""

import io
import os
import sys
import time
from contextlib import contextmanager
from unittest.mock import patch

import pytest

from pykit.logging import Colors

# Import the logging package
from pykit.logging import TerminalLogger
from pykit.logging import log_debug
from pykit.logging import log_error
from pykit.logging import log_group_end
from pykit.logging import log_group_start
from pykit.logging import log_info
from pykit.logging import log_step_end
from pykit.logging import log_step_start
from pykit.logging import log_success
from pykit.logging import log_warning
from pykit.logging import log_workflow_end
from pykit.logging import log_workflow_start
from pykit.logging.logger import _global_logger


@contextmanager
def capture_stderr():
    """Context manager to capture stderr output"""
    old_stderr = sys.stderr
    sys.stderr = captured_output = io.StringIO()
    try:
        yield captured_output
    finally:
        sys.stderr = old_stderr


class TestColors:
    """Test color constants"""

    def test_color_codes_defined(self):
        """Test that all color codes are properly defined"""
        assert Colors.RED == "\033[0;31m"
        assert Colors.GREEN == "\033[0;32m"
        assert Colors.YELLOW == "\033[0;33m"
        assert Colors.BLUE == "\033[0;34m"
        assert Colors.CYAN == "\033[0;36m"
        assert Colors.PURPLE == "\033[0;35m"
        assert Colors.BOLD == "\033[1m"
        assert Colors.WHITE == "\033[0;37m"
        assert Colors.NC == "\033[0m"


class TestTerminalLoggerInitialization:
    """Test Logger class initialization and configuration"""

    def test_default_initialization(self):
        """Test logger with default settings"""
        logger = TerminalLogger()
        assert logger.debug_mode is False
        assert logger.error_trap is False
        assert logger.current_workflow is None
        assert logger.current_step is None
        assert logger.current_group is None
        assert logger.workflow_start_time is None
        assert logger.step_start_time is None

    def test_initialization_with_params(self):
        """Test logger with custom parameters"""
        logger = TerminalLogger(debug_mode=True, error_trap=True)
        assert logger.debug_mode is True
        assert logger.error_trap is True

    def test_initialization_with_env_vars(self):
        """Test logger initialization from environment variables"""
        with patch.dict(os.environ, {"DEBUG_MODE": "true", "ERROR_TRAP": "true"}):
            logger = TerminalLogger()
            assert logger.debug_mode is True
            assert logger.error_trap is True

        with patch.dict(os.environ, {"DEBUG_MODE": "false", "ERROR_TRAP": "false"}):
            logger = TerminalLogger()
            assert logger.debug_mode is False
            assert logger.error_trap is False


class TestBasicLogging:
    """Test basic logging functionality"""

    def test_info_logging(self):
        """Test info message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.info("Test info message")

        result = output.getvalue()
        assert "💡 Test info message" in result
        assert Colors.CYAN in result
        assert Colors.NC in result

    def test_success_logging(self):
        """Test success message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.success("Test success message")

        result = output.getvalue()
        assert "🎉 Test success message" in result
        assert Colors.GREEN in result
        assert Colors.NC in result

    def test_error_logging(self):
        """Test error message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.error("Test error message")

        result = output.getvalue()
        assert "💥 Test error message" in result
        assert Colors.RED in result
        assert Colors.NC in result

    def test_warning_logging(self):
        """Test warning message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.warning("Test warning message")

        result = output.getvalue()
        assert "🚨 Test warning message" in result
        assert Colors.YELLOW in result
        assert Colors.NC in result

    def test_debug_logging_enabled(self):
        """Test debug message when debug mode is enabled"""
        logger = TerminalLogger(debug_mode=True)
        with capture_stderr() as output:
            logger.debug("Test debug message")

        result = output.getvalue()
        assert "🐛 DEBUG: Test debug message" in result
        assert Colors.PURPLE in result
        assert Colors.NC in result

    def test_debug_logging_disabled(self):
        """Test debug message when debug mode is disabled"""
        logger = TerminalLogger(debug_mode=False)
        with capture_stderr() as output:
            logger.debug("Test debug message")

        result = output.getvalue()
        assert result == ""  # Should be empty when debug is disabled

    def test_notice_logging(self):
        """Test notice message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.notice("Test notice message")

        result = output.getvalue()
        assert "💡 NOTICE: Test notice message" in result
        assert Colors.BLUE in result
        assert Colors.NC in result


class TestStructuredLogging:
    """Test structured logging (headers, sections, etc.)"""

    def test_header_logging(self):
        """Test header message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.header("Test Header")

        result = output.getvalue()
        assert "🎯 Test Header" in result
        assert Colors.BOLD in result
        assert Colors.BLUE in result
        assert Colors.NC in result

    def test_section_logging(self):
        """Test section message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.section("Test Section")

        result = output.getvalue()
        assert "Test Section" in result
        assert Colors.CYAN in result
        assert Colors.NC in result

    def test_subsection_logging(self):
        """Test subsection message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.subsection("Test Subsection")

        result = output.getvalue()
        assert "  Test Subsection" in result
        assert Colors.BOLD in result
        assert Colors.CYAN in result
        assert Colors.NC in result

    def test_section_info_logging(self):
        """Test section info message logging"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.section_info("Test section info")

        result = output.getvalue()
        assert "    Test section info" in result
        assert Colors.WHITE in result
        assert Colors.NC in result

    def test_phase_logging(self):
        """Test phase message with separators"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.phase("Test Phase")

        result = output.getvalue()
        assert "Test Phase" in result
        assert "=" in result  # Should contain separator
        assert Colors.BOLD in result
        assert Colors.PURPLE in result
        assert Colors.NC in result

    def test_bold_message_logging(self):
        """Test bold message with separators"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.bold_message("Test Bold Message")

        result = output.getvalue()
        assert "Test Bold Message" in result
        assert "=" in result  # Should contain separator
        assert Colors.GREEN in result
        assert Colors.BOLD in result
        assert Colors.NC in result


class TestWorkflowTracking:
    """Test workflow tracking functionality"""

    def test_workflow_start(self):
        """Test workflow start tracking"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.workflow_start("Test Workflow")

        result = output.getvalue()
        assert "🚀 Starting workflow: Test Workflow" in result
        assert Colors.BOLD in result
        assert Colors.PURPLE in result
        assert Colors.NC in result
        assert logger.current_workflow == "Test Workflow"
        assert logger.workflow_start_time is not None

    def test_workflow_end_success(self):
        """Test workflow end with success status"""
        logger = TerminalLogger()
        logger.workflow_start("Test Workflow")
        time.sleep(0.1)  # Small delay to test duration

        with capture_stderr() as output:
            logger.workflow_end("Test Workflow", "success")

        result = output.getvalue()
        assert "✅ Workflow completed: Test Workflow" in result
        assert "in" in result and "s" in result  # Duration should be included
        assert Colors.BOLD in result
        assert Colors.GREEN in result
        assert Colors.NC in result

    def test_workflow_end_failure(self):
        """Test workflow end with failure status"""
        logger = TerminalLogger()
        logger.workflow_start("Test Workflow")
        time.sleep(0.1)  # Small delay to test duration

        with capture_stderr() as output:
            logger.workflow_end("Test Workflow", "failure")

        result = output.getvalue()
        assert "❌ Workflow failed: Test Workflow" in result
        assert "in" in result and "s" in result  # Duration should be included
        assert Colors.BOLD in result
        assert Colors.RED in result
        assert Colors.NC in result


class TestStepTracking:
    """Test step tracking functionality"""

    def test_step_start(self):
        """Test step start tracking"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.step_start("Test Step", 1, 3)

        result = output.getvalue()
        assert "[1/3] Test Step" in result
        assert Colors.BOLD in result
        assert Colors.BLUE in result
        assert Colors.NC in result
        assert logger.current_step == "Test Step"
        assert logger.step_start_time is not None

    def test_step_end_success(self):
        """Test step end with success status"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.step_end("Test Step", "success")

        result = output.getvalue()
        assert "✓ Test Step completed" in result
        assert Colors.GREEN in result
        assert Colors.NC in result

    def test_step_end_failure(self):
        """Test step end with failure status"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.step_end("Test Step", "failure")

        result = output.getvalue()
        assert "✗ Test Step failed" in result
        assert Colors.RED in result
        assert Colors.NC in result

    def test_step_end_with_timing(self):
        """Test step end with timing information"""
        logger = TerminalLogger()
        logger.step_start("Test Step", 1, 1)
        time.sleep(0.1)  # Small delay to test duration

        with capture_stderr() as output:
            logger.step_end_with_timing("Test Step", "success")

        result = output.getvalue()
        assert "✓ Test Step completed" in result
        assert "in" in result and "s" in result  # Duration should be included
        assert Colors.GREEN in result
        assert Colors.NC in result


class TestGroupTracking:
    """Test group tracking functionality"""

    def test_group_start(self):
        """Test group start tracking"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.group_start("Test Group")

        result = output.getvalue()
        assert "▶ Test Group" in result
        assert Colors.CYAN in result
        assert Colors.NC in result
        assert logger.current_group == "Test Group"

    def test_group_end(self):
        """Test group end tracking"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.group_end("Test Group")

        result = output.getvalue()
        assert "◀ End: Test Group" in result
        assert Colors.CYAN in result
        assert Colors.NC in result
        assert logger.current_group is None

    def test_group_context_manager(self):
        """Test group as context manager"""
        logger = TerminalLogger()
        with capture_stderr() as output, logger.group("Test Group"):
            logger.info("Inside group")

        result = output.getvalue()
        assert "▶ Test Group" in result
        assert "💡 Inside group" in result
        assert "◀ End: Test Group" in result
        assert logger.current_group is None  # Should be reset after context


class TestErrorHandling:
    """Test error handling functionality"""

    def test_handle_error_basic(self):
        """Test basic error handling"""
        logger = TerminalLogger(error_trap=False)  # Don't exit for test

        with capture_stderr() as output:
            logger.handle_error("Test error occurred")

        result = output.getvalue()
        assert "💥 Test error occurred" in result
        assert Colors.RED in result
        assert Colors.NC in result

    def test_handle_error_with_recovery_hint(self):
        """Test error handling with recovery hint"""
        logger = TerminalLogger(error_trap=False)  # Don't exit for test

        with capture_stderr() as output:
            logger.handle_error("Test error", recovery_hint="Try again later")

        result = output.getvalue()
        assert "💥 Test error" in result
        assert "💡 NOTICE: Recovery hint: Try again later" in result

    def test_handle_error_with_workflow(self):
        """Test error handling with active workflow"""
        logger = TerminalLogger(error_trap=False)  # Don't exit for test
        logger.workflow_start("Test Workflow")

        with capture_stderr() as output:
            logger.handle_error("Test error")

        result = output.getvalue()
        assert "💥 Test error" in result
        assert "❌ Workflow failed: Test Workflow" in result

    def test_handle_error_with_exit_trap(self):
        """Test error handling with exit trap enabled"""
        logger = TerminalLogger(error_trap=True)

        test_exit_code = 42
        with pytest.raises(SystemExit) as exc_info:
            logger.handle_error("Test error", exit_code=test_exit_code)

        assert exc_info.value.code == test_exit_code


class TestUtilityMethods:
    """Test utility methods"""

    def test_get_duration(self):
        """Test duration calculation"""
        logger = TerminalLogger()
        start_time = time.time()
        time.sleep(0.1)  # Sleep for 100ms
        duration = logger._get_duration(start_time)
        assert duration >= 0  # Should be at least 0 seconds
        assert isinstance(duration, int)

    def test_get_duration_none(self):
        """Test duration calculation with None start time"""
        logger = TerminalLogger()
        duration = logger._get_duration(None)
        assert duration == 0

    def test_step_method(self):
        """Test step method with numbering"""
        logger = TerminalLogger()
        with capture_stderr() as output:
            logger.step(2, 5, "Processing data")

        result = output.getvalue()
        assert "[2/5]" in result
        assert "Processing data" in result
        assert Colors.BOLD in result
        assert Colors.BLUE in result
        assert Colors.CYAN in result
        assert Colors.NC in result


class TestSimpleAPIFunctions:
    """Test simple API functions (like print)"""

    def test_log_info_function(self):
        """Test log_info simple function"""
        with capture_stderr() as output:
            log_info("Test info")

        result = output.getvalue()
        assert "💡 Test info" in result
        assert Colors.CYAN in result
        assert Colors.NC in result

    def test_log_success_function(self):
        """Test log_success simple function"""
        with capture_stderr() as output:
            log_success("Test success")

        result = output.getvalue()
        assert "🎉 Test success" in result
        assert Colors.GREEN in result
        assert Colors.NC in result

    def test_log_error_function(self):
        """Test log_error simple function"""
        with capture_stderr() as output:
            log_error("Test error")

        result = output.getvalue()
        assert "💥 Test error" in result
        assert Colors.RED in result
        assert Colors.NC in result

    def test_log_warning_function(self):
        """Test log_warning simple function"""
        with capture_stderr() as output:
            log_warning("Test warning")

        result = output.getvalue()
        assert "🚨 Test warning" in result
        assert Colors.YELLOW in result
        assert Colors.NC in result

    def test_log_debug_function(self):
        """Test log_debug simple function"""
        # Test with debug disabled (default)
        with capture_stderr() as output:
            log_debug("Test debug")
        result = output.getvalue()
        assert result == ""  # Should be empty

        # Test with debug enabled
        with patch.dict(os.environ, {"DEBUG_MODE": "true"}):
            # Need to recreate the global logger to pick up env change
            _global_logger.debug_mode = True

            with capture_stderr() as output:
                log_debug("Test debug")
            result = output.getvalue()
            assert "🐛 DEBUG: Test debug" in result
            assert Colors.PURPLE in result
            assert Colors.NC in result

    def test_log_workflow_functions(self):
        """Test workflow simple functions"""
        with capture_stderr() as output:
            log_workflow_start("Test Workflow")
            log_workflow_end("Test Workflow", "success")

        result = output.getvalue()
        assert "🚀 Starting workflow: Test Workflow" in result
        assert "✅ Workflow completed: Test Workflow" in result

    def test_log_step_functions(self):
        """Test step simple functions"""
        with capture_stderr() as output:
            log_step_start("Test Step", 1, 2)
            log_step_end("Test Step", "success")

        result = output.getvalue()
        assert "[1/2] Test Step" in result
        assert "✓ Test Step completed" in result

    def test_log_group_functions(self):
        """Test group simple functions"""
        with capture_stderr() as output:
            log_group_start("Test Group")
            log_group_end("Test Group")

        result = output.getvalue()
        assert "▶ Test Group" in result
        assert "◀ End: Test Group" in result


class TestIntegrationScenarios:
    """Test integration scenarios similar to real usage"""

    def test_complete_workflow_scenario(self):
        """Test a complete workflow scenario"""
        logger = TerminalLogger()

        with capture_stderr() as output:
            # Complete workflow
            logger.workflow_start("User Registration")

            logger.step_start("Validate Input", 1, 3)
            logger.info("Checking email format")
            logger.step_end("Validate Input", "success")

            logger.step_start("Create Account", 2, 3)
            with logger.group("Database Operations"):
                logger.info("Inserting user record")
                logger.success("User created successfully")
            logger.step_end("Create Account", "success")

            logger.step_start("Send Welcome Email", 3, 3)
            logger.info("Preparing email template")
            logger.warning("SMTP server slow response")
            logger.step_end("Send Welcome Email", "success")

            logger.workflow_end("User Registration", "success")

        result = output.getvalue()

        # Check all components are present
        assert "🚀 Starting workflow: User Registration" in result
        assert "[1/3] Validate Input" in result
        assert "[2/3] Create Account" in result
        assert "[3/3] Send Welcome Email" in result
        assert "▶ Database Operations" in result
        assert "◀ End: Database Operations" in result
        assert "✅ Workflow completed: User Registration" in result

    def test_error_scenario_workflow(self):
        """Test workflow with error scenario"""
        logger = TerminalLogger(error_trap=False)  # Don't exit for test

        with capture_stderr() as output:
            logger.workflow_start("Data Processing")

            logger.step_start("Load Data", 1, 2)
            logger.info("Reading input file")
            logger.error("File not found: data.csv")
            logger.step_end("Load Data", "failure")

            # Workflow should fail
            logger.handle_error("Critical error in data processing", recovery_hint="Check file path and permissions")

        result = output.getvalue()

        assert "🚀 Starting workflow: Data Processing" in result
        assert "[1/2] Load Data" in result
        assert "💥 File not found: data.csv" in result
        assert "✗ Load Data failed" in result
        assert "💥 Critical error in data processing" in result
        assert "💡 NOTICE: Recovery hint: Check file path and permissions" in result
        assert "❌ Workflow failed: Data Processing" in result


class TestThreadSafety:
    """Test thread safety considerations"""

    def test_multiple_logger_instances(self):
        """Test that multiple logger instances don't interfere"""
        logger1 = TerminalLogger()
        logger2 = TerminalLogger()

        # Set different contexts
        logger1.set_workflow_context("Workflow 1")
        logger2.set_workflow_context("Workflow 2")

        assert logger1.current_workflow == "Workflow 1"
        assert logger2.current_workflow == "Workflow 2"
        assert logger1.current_workflow != logger2.current_workflow


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
