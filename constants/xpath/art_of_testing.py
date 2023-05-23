btn_gen_alert_box = "//button[contains(text(), 'Generate Alert Box')]"
# btn_submit = "//button[@type='button']"
btn_submit = "//button[@id='idOfButton']"
txt_box = "//input[@type='text']"
h2_useful_resources = "//h2[contains(text(), 'Useful Resources')]" 
#h2_useful_resources = "//h2[text()='Useful Resources')]"
# contains() will locate any h2 element that contains the specified text, even if there are additional words or 
# characters within the element's text node, whereas text() will only locate the h2 element that exactly matches the specified text.
drop_down = "//select[contains(@id, 'testingDropdown')]"
drop_down = "//select[@id='testingDropdown']"
lnk_link_text = "//a[contains(text(),'link')]"
txt_copy_year = "//div[@class='copyright-bar']//br"