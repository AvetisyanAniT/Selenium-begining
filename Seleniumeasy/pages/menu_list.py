from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestGoRadiobuttonsPage:
    URL = 'https://www.seleniumeasy.com/test/'
    POPUP = (By.ID, 'at-cv-lightbox-header')
    CLOSEBUTTON = (By.ID, 'at-cv-lightbox-close')
    TREEMENU = (By.ID, 'treemenu')
    INPUTFORMS = (By.LINK_TEXT, 'Input Forms')
    RADIOBUTTONSDEMO = (By.LINK_TEXT, 'Radio Buttons Demo')

    def __init__(self, driver):
        self.driver = driver

    def test_load(self):
        self.driver.get(self.URL)

    def test_close_popup(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.POPUP))
            )
            self.driver.find_element(*self.CLOSEBUTTON).click()
        except:
            print('No popup displayed')

    def test_scroll_to_menu_list(self):
        treemenu = self.driver.find_element(*self.TREEMENU)
        self.driver.execute_script('arguments[0].scrollIntoView();', treemenu)
    
    def test_open_radiobutton_demo(self):
        self.driver.find_element(*self.INPUTFORMS).click()
        self.driver.find_element(*self.RADIOBUTTONSDEMO).click()