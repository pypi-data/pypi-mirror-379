# Riso Python Kit

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![PyPI - Version](https://img.shields.io/pypi/v/riso-toolkit)](https://pypi.org/project/riso-toolkit/)


RisoTech Python Kit provides a set of utilities, components, and best practices to enhance the functionality of Riso-based Python applications.

## Features

### Terminal Logging Package (`pykit.logging`)

A colorful terminal logging system converted from bash script to Python, providing:

- 🎨 **Colorful terminal output** with ANSI color codes
- 📊 **Workflow tracking** with timing and context management
- 📋 **Step-by-step logging** with progress indicators
- 📦 **Group logging** with context managers
- 🚨 **Error handling** with recovery hints
- 🐛 **Debug mode** support

#### Quick Usage

**Simple logging (like print()):**
```python
from pykit.logging import log_info, log_success, log_error, log_warning

log_info("This works like print but with colors!")
log_success("Operation completed successfully!")
log_error("Something went wrong!")
log_warning("This is a warning!")
```

**Advanced workflow logging:**
```python
from pykit.logging import TerminalLogger

logger = TerminalLogger()
logger.workflow_start("Data Processing")

logger.step_start("Load Data", 1, 3)
logger.info("Loading data from database...")
logger.step_end("Load Data", "success")

with logger.group("Data Transformation"):
    logger.info("Applying transformations...")
    logger.success("Transformations completed")

logger.workflow_end("Data Processing", "success")
```
