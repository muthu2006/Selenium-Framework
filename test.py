import time
# from basic_functions import open_browser_to_link, click_element, enter_text_in_element, scroll_element_into_view, select_value_in_dropdown, handle_alert
# from basic_functions import *
from library.basic_selenium_actions import *
from constants.xpath.art_of_testing import *

driver = open_browser_to_link("https://artoftesting.com/samplesiteforselenium")

#wait_until_element_is_visible(driver, "//button[@id='idOfButton']")
#click_element(driver, "//button[@id='idOfButton']")
wait_until_element_is_visible(driver, btn_submit)
click_element(driver, btn_submit)

#wait_until_element_is_visible(driver, "//input[@type='text']")
#enter_text_in_element(driver, "//input[@type='text']", "Automation")
wait_until_element_is_visible(driver, txt_box)
enter_text_in_element(driver, txt_box, "Automation")

#wait_until_element_is_visible(driver, "//h2[contains(text(), 'Useful Resources')]")
#scroll_element_into_view(driver, "//h2[contains(text(), 'Useful Resources')]")
wait_until_element_is_visible(driver, h2_useful_resources)
scroll_element_into_view(driver, h2_useful_resources)

#wait_until_element_is_visible(driver, "//select[@id='testingDropdown']")
#scroll_element_into_view(driver, "//select[@id='testingDropdown']")
wait_until_element_is_visible(driver, drop_down)
scroll_element_into_view(driver, drop_down)
select_value_in_dropdown(driver, drop_down, "Manual")

#wait_until_element_is_visible(driver, "//button[contains(text(), 'Generate Alert Box')]")
#click_element(driver, "//button[contains(text(), 'Generate Alert Box')]")
wait_until_element_is_visible(driver, btn_gen_alert_box)
click_element(driver, btn_gen_alert_box)
alert_text = handle_alert(driver)
print(f'alert text is {alert_text}')
time.sleep(30)

