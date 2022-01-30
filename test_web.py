import pytest
from Seleniumeasy.pages.Base_page import TestBase
from Seleniumeasy.pages.menu_list import TestGoRadiobuttonsPage
from Seleniumeasy.pages.radiobutton_page import TestClickRadiobuttons

# Activate Chrome browser
driver = TestBase().test_driver()

# Set up test case data
WORD = 'Male'

menu_list = TestGoRadiobuttonsPage(driver)
menu_list.test_load()

# Close opened popup, if popup exist
menu_list.test_close_popup()

# Scroll to Menu List
menu_list.test_scroll_to_menu_list()

# Click on "Radio buttons Demo"
menu_list.test_open_radiobutton_demo()

# Choose Male Radiobutton under "Radio Button Demo" section
radiobutton_page = TestClickRadiobuttons(driver)
radiobutton_page.test_click_radiobutton_male()

# Click Get check value button
radiobutton_page.test_click_button_check()

# Check that Male word exist in message, if not, save screenshot
radiobutton_page.test_check_word(WORD)

# assert radiobutton_page.test_word(WORD)

# close browser
# driver.close()

print('Selenium sixth task test case successfully completed')