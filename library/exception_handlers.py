import logging
import sys
from .basic_selenium_actions import take_screenshot

# Configure logging
logging.basicConfig (
    filename='automation.log', # Specify the log file path
    level=logging.INFO, # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' # Specify the log message format
)

def continue_on_failure(driver, function, *args, **kwargs):
    # args is a list of unnamed arguments
    # kwargs is the list of named arguments - dictionary
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.error(e)
        take_screenshot(driver)

def terminate_on_failure(driver, function, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.error(e)
        take_screenshot(driver)
        sys.exit()

def ignore_error(driver, function, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.info(e)
        take_screenshot(driver)

def expect_error(driver, function, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.info("Expected error occured" + str(e))
        take_screenshot(driver) 
    else:
        take_screenshot(driver)
        raise AssertionError("Expected error not raised.")