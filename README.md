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

# Data Aggregation Utility
This Python utility provides functions for aggregating data from multiple sources. It allows users to input data from the command line prompt, handles invalid input gracefully, aggregates the data from multiple sources, and prints the aggregated data.

## Features
Accepts data from multiple sources provided by the user.
Handles invalid input gracefully, printing an error message and continuing to prompt for input.
Aggregates data from all sources into a single list.
Provides an example usage in the main part of the code.
## Installation
No installation is required. Simply download the data_aggregation.py file and run it using a Python interpreter.

## Usage
To use the utility, follow these steps:

Run the data_aggregation.py file using a Python interpreter.
Follow the prompts to enter data for each source. Separate values by spaces and leave empty to finish entering data.
After entering data for all sources, the utility will aggregate the data and print the aggregated result.
Example usage:

kotlin
Copy code
$ python data_aggregation.py
Enter data (separate values by spaces, leave empty to finish): 1 2 3
Enter data (separate values by spaces, leave empty to finish): 4 5 6
Enter data (separate values by spaces, leave empty to finish): 7 8
Enter data (separate values by spaces, leave empty to finish): 
Aggregated Data: [1, 2, 3, 4, 5, 6, 7, 8]




