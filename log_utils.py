import logging

def log_message(level, *messages):
    """
    Log multiple messages with different levels of severity.

    Parameters:
        level: int
            The severity level of the log messages.
        *messages: tuple
            Variable number of messages to be logged.
    """
    """Configure logging"""
    if level == 1:
        log_level = logging.DEBUG
    elif level == 2:
        log_level = logging.INFO
    elif level == 3:
        log_level = logging.WARNING
    elif level == 4:
        log_level = logging.ERROR
    elif level == 5:
        log_level = logging.CRITICAL
    else:
        log_level = logging.INFO

    """ Log each message with the determined logging level"""
    for message in messages:
        logging.log(log_level, message)

# Example usage
log_message(1, "This is a Debug message", "Another debug message")
log_message(3, "Warning: Something unexpected happened")
log_message(4, "Error: An error occurred while processing data")
