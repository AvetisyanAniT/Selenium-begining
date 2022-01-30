

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestDuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def test_load(self):
        self.browser.get(self.URL)

    def test_search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)


