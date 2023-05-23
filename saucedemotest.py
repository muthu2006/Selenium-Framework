from library.basic_selenium_actions import *
from library.comparison_actions import *
from library.data_helper import *
from constants.xpath.art_of_testing import *
from constants.xpath.saucedemo import *
from library.exception_handlers import *
import time

data = read_csv_data("D:/Selenium Framework/constants/data/saucedemo_login.csv")
driver = open_browser("https://www.saucedemo.com/")
wait_until_element_is_visible(driver, txt_box_username)
enter_text_in_element(driver, txt_box_username, 'standard_user')
enter_text_in_element(driver, txt_box_password, 'secret_sauce')
click_element(driver, btn_login)
time.sleep(2)
wait_until_element_is_visible(driver, lnk_backpack)
click_element(driver, lnk_backpack)
wait_until_element_is_clickable(driver, btn_add_to_cart)
time.sleep(2)
click_element(driver, btn_add_to_cart)
wait_until_element_is_visible(driver, btn_remove)
time.sleep(10)