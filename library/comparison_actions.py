# from library.basic_selenium_actions import get_element_text > library.xx works but not recommended
from .basic_selenium_actions import get_element_text # . means same directory as
import logging

# Configure logging
logging.basicConfig (
    filename='comparison.log', # Specify the log file path
    level=logging.INFO, # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' # Specify the log message format
)

def should_be_equal(driver, xpath, expected_value):
    element_text = get_element_text(driver, xpath)
    try:
        assert element_text == expected_value
        #print(f"Assertion passed, text [{element_text}] equal to expected text [{expected_value}].")
        logging.info(f"Assertion passed, text [{element_text}] equal to expected text [{expected_value}].")
    except AssertionError as e: # e refers the AssertionError
        #print(f"Assetion failed, text [{element_text}] not equal to expected text [{expected_value}].")
        logging.error(f"Assetion failed, text [{element_text}] not equal to expected text [{expected_value}].")
        raise AssertionError

def should_be_equal_as_strings(driver, xpath, expected_text, lowercase = False):
    element_text = get_element_text(driver, xpath)
    try:
        if lowercase:
            assert str(element_text).lower() == str(expected_text).lower()
            #print(f"Assertion passed, string [{element_text}] equal to expected string [{expected_text}].")
            logging.info(f"Assertion passed, string [{element_text}] equal to expected string [{expected_text}].")
        else:
            assert str(element_text) == str(expected_text)
            #print(f"Assertion passed, string [{element_text}] equal to expected string [{expected_text}].")
            logging.info(f"Assertion passed, string [{element_text}] equal to expected string [{expected_text}].")
    except AssertionError as e: # e refers the AssertionError
        #print(f"Assetion failed, string [{element_text}] not equal to expected string [{expected_text}].")
        logging.error(f"Assetion failed, string [{element_text}] not equal to expected string [{expected_text}].")
        raise AssertionError

def should_be_equal_as_integers(driver, xpath, expected_number):
    element_text = get_element_text(driver, xpath)
    try:
        assert int(element_text) == int(expected_number)
        #print(f"Assertion passed, text [{element_text}] equal to expected number [{expected_number}].")
        logging.info(f"Assertion passed, text [{element_text}] equal to expected number [{expected_number}].")
    except AssertionError as e: # e refers the AssertionError
        #print(f"Assetion failed, text [{element_text}] not equal to expected number [{expected_number}].")
        logging.error(f"Assetion failed, text [{element_text}] not equal to expected number [{expected_number}].")
        raise AssertionError

def should_be_empty(driver, xpath):
    element_text = get_element_text(driver, xpath)
    try:
        assert element_text == None or len(element_text) == 0
        #print(f"Assertion passed, element text is empty.")
        logging.info(f"Assertion passed, element text is empty.")
    except AssertionError as e: # e refers the AssertionError
        #print(f"Assetion failed, element text is [{element_text}]")
        logging.error(f"Assetion failed, element text is [{element_text}]")
        raise AssertionError

def should_contain(driver, xpath, expected_text):
    element_text = get_element_text(driver, xpath)
    try:
        assert expected_text in element_text
        #print(f"Assertion passed, string [{element_text}] contains [{expected_text}].")
        logging.info(f"Assertion passed, string [{element_text}] contains [{expected_text}].")
    except AssertionError as e: # e refers the AssertionError
        #print(f"Assertion failed, string [{element_text}[] does not contains [{expected_text}].")   
        #logging.error(f"Assertion failed, string [{element_text}[] does not contains [{expected_text}].")
        raise AssertionError(f"{e}: Assertion failed, string [{element_text}[] does not contains [{expected_text}].")