from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print('Selenium first task test case started')
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')
driver.maximize_window()

#navigate to the url
driver.get('https://www.facebook.com/')

#search & enter the Email or Phone field & enter Password
driver.find_element_by_id('email').send_keys('testemail@gmail.com')
driver.find_element_by_id('pass').send_keys('testpass')
time.sleep(1)

#click Login
driver.find_element_by_name('login').send_keys(Keys.ENTER)
time.sleep(1)

#close the browser
driver.close()
print('Selenium first task test case successfully completed')