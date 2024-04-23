# Python Logging Utils
Python Logging Utils is a collection of utility functions for logging in Python applications. It provides functions to log multiple messages with different levels of severity in a single function call.

## Installation
You can install Python Logging Utils using pip:


--pip install python-logging-utils
## Usage
To use Python Logging Utils in your Python code, simply import the log_message function and call it with the desired severity level and messages:


from logging_utils import log_message

# Log debug messages
log_message(1, "This is a debug message", "Another debug message")

# Log warning message
log_message(3, "Warning: Something unexpected happened")

# Log error message
log_message(4, "Error: An error occurred while processing data")
