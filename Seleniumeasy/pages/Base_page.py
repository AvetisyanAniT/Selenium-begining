from selenium import webdriver

class TestBase:
    def test_driver(self):
        driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')
        driver.maximize_window()
        return driver