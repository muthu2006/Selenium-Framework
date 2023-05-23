from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

# function to open browser and navigate to a URL
def open_browser_to_link(url):
    # set the driver path
    service = Service("D:/Selenium Framework/Constants/Driver/chromedriver.exe")
    # create a Chrome driver instance
    driver = webdriver.Chrome(service=service)
    # maximize the window
    driver.maximize_window()
    # navigate to the URL
    driver.get(url)
    # return the driver instance
    return driver

# function to click an element identified by XPATH
def click_element(driver, xpath):
    # set a wait period of 10 seconds for the element to be clickable
    wait = WebDriverWait(driver, 10)
    # get the element identified by the XPATH
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    # click the element
    element.click()

# function to enter text in an element identified by XPATH
def enter_text_in_element(driver, xpath, text):
    # set a wait period of 10 seconds for the element to be clickable
    wait = WebDriverWait(driver, 10)
    # get the element identified by the XPATH
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    # enter the provided text into the element
    element.send_keys(text)

# function to get the text of an element identified by XPATH
def get_element_text(driver, xpath):
    # set a wait period of 10 seconds for the element to be clickable
    wait = WebDriverWait(driver, 10)
    # get the element identified by the XPATH
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    # return the text of the element
    return element.text

# function to scroll an element identified by XPATH into view
def scroll_element_into_view(driver, xpath):
    # find the element identified by the XPATH
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC._element_if_visible((By.XPATH, xpath))) -> element = driver.find_element(By.XPATH, xpath)
    element = driver.find_element(By.XPATH, xpath)
    # scroll the element into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element)

# function to select a value from a dropdown identified by XPATH
def select_value_in_dropdown(driver, xpath, value):
    # set a wait period of 10 seconds for the element to be clickable
    wait = WebDriverWait(driver, 10)
    # get the element identified by the XPATH
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
     # create a Select object for the dropdown element
    dropdown = Select(element)
    # select the provided value from the dropdown
    dropdown.select_by_value(value)

# function to handle an alert popup
def handle_alert(driver, accept=True):
    # create an Alert object for the popup
    alert = Alert(driver)
    # get the text of the popup message
    alert_text_message = alert.text
    # accept or dismiss the popup based on provided argument
    if accept:
        alert.accept()
    else:
        alert.dismiss()
    # return the text of the popup message
    return alert_text_message

# function to wait for an element identified by XPATH to be visible
def wait_until_element_is_visible(driver, xpath, wait_time=10):
    # set a wait period of 10 seconds for the element to be visible
    wait = WebDriverWait(driver, 10)
    try:
        # waiting for the element to be visible within given wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        # if element is found, returning the element found message
        if element:
            return f"Element found: {xpath}."
    except Exception as e:
        # if element is not found, returning the element not found message
        print(f"{e}: Element not found: {xpath}.") 