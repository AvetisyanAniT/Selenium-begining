from selenium.webdriver.common.by import By

class TestClickRadiobuttons:
    MALEBUTTON = (By.XPATH, "//input[@value = 'Male' and @name = 'optradio']")
    CHECKVALUEBUTTON = (By.ID, 'buttoncheck')
    CHECKTEXT = (By.CSS_SELECTOR, "p.radiobutton")

    # @classmethod
    # def test_CHECK_WORD(cls, word):
    #     xpath = f"//p[contains(text(), '{word}')]"
    #     return (By.XPATH, xpath)

    def __init__(self, driver):
        self.driver = driver

    def test_click_radiobutton_male(self):
        self.driver.find_element(*self.MALEBUTTON).click()

    def test_click_button_check(self):
        self.driver.find_element(*self.CHECKVALUEBUTTON).click()
    
    def test_word(self, word):
        text = self.driver.find_element(*self.test_CHECK_WORD(word)).text

    def test_check_word(self, word):
        text = self.driver.find_element(*self.CHECKTEXT).text
        if word in text:
            pass
            # print('ok')
        else:
            # print('not ok')
            self.driver.save_screenshot("D:\QA Auto\lesson16\male_in_text.png")