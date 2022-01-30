from selenium import webdriver

class TestBase:

    def test_browser(self):
        browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')
        return browser
