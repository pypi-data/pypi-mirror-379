#!/usr/bin/env python3
"""
Demo script to showcase the Riso PyKit TerminalLogger package

This script demonstrates all the features converted from logger.sh to Python.
Run this to see the colorful terminal logging in action.
"""

import os
import sys
import time
from pathlib import Path

# Add the parent directory to sys.path so we can import pykit
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the logging package
from pykit.logging import TerminalLogger
from pykit.logging import display_bold_message
from pykit.logging import log_debug
from pykit.logging import log_error
from pykit.logging import log_info
from pykit.logging import log_notice
from pykit.logging import log_phase
from pykit.logging import log_step_end
from pykit.logging import log_step_start
from pykit.logging import log_success
from pykit.logging import log_warning
from pykit.logging import log_workflow_end
from pykit.logging import log_workflow_start


def demo_simple_logging():
    """Demo simple logging functions (like using print)"""
    log_phase("Simple Logging Demo")

    log_info("This is an information message")
    log_success("Operation completed successfully!")
    log_warning("This is a warning message")
    log_error("This is an error message")
    log_notice("This is a notice message")
    log_debug("This is a debug message")

    time.sleep(0.5)


def demo_workflow_tracking():
    """Demo workflow and step tracking"""
    log_phase("Workflow Tracking Demo")

    # Start a workflow
    log_workflow_start("User Registration Process")

    # Step 1
    log_step_start("Validate Input", 1, 3)
    time.sleep(0.3)
    log_info("Checking email format...")
    log_info("Validating password strength...")
    log_step_end("Validate Input", "success")

    # Step 2
    log_step_start("Create Database Record", 2, 3)
    time.sleep(0.3)
    log_info("Connecting to database...")
    log_info("Inserting user record...")
    log_step_end("Create Database Record", "success")

    # Step 3
    log_step_start("Send Welcome Email", 3, 3)
    time.sleep(0.3)
    log_info("Preparing email template...")
    log_info("Sending welcome email...")
    log_step_end("Send Welcome Email", "success")

    # End workflow
    log_workflow_end("User Registration Process", "success")

    time.sleep(0.5)


def demo_terminal_logger_class():
    """Demo using the TerminalLogger class directly"""
    log_phase("TerminalLogger Class Demo")

    # Create a logger instance with debug mode enabled
    logger = TerminalLogger(debug_mode=True)

    logger.workflow_start("Advanced Processing Workflow")

    with logger.group("Initialization Phase"):
        logger.info("Loading configuration...")
        logger.debug("Config file path: /etc/myapp/config.yml")
        logger.info("Initializing modules...")
        logger.debug("Loaded 15 modules successfully")
        logger.success("Initialization completed")

    logger.step_start("Data Analysis", 1, 2)
    with logger.group("Statistical Analysis"):
        logger.info("Computing statistical metrics...")
        logger.debug("Processing 10,000 data points")
        logger.info("Generating reports...")
        logger.success("Statistical analysis completed")
    logger.step_end_with_timing("Data Analysis", "success")

    logger.step_start("Report Generation", 2, 2)
    logger.info("Compiling final report...")
    logger.info("Generating visualizations...")
    logger.step_end_with_timing("Report Generation", "success")

    logger.workflow_end("Advanced Processing Workflow", "success")


def main():
    """Run all demos"""
    print("🎯 Riso PyKit TerminalLogger Package Demo")
    print("=" * 50)
    print("Converting logger.sh functionality to Python...")
    print("=" * 50)

    time.sleep(1)

    # Run all demos
    demo_simple_logging()
    demo_workflow_tracking()
    demo_terminal_logger_class()

    display_bold_message("🎉 Demo completed! TerminalLogger is working perfectly! 🎉")

    print("\n" + "=" * 50)
    print("🔧 You can now use pykit.logging.TerminalLogger in your Python code!")
    print("=" * 50)


if __name__ == "__main__":
    # Enable debug mode for demo
    os.environ["DEBUG_MODE"] = "true"
    main()
