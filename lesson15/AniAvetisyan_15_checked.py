from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

print('Selenium forth task test case started')

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')
driver.maximize_window()

driver.get('https://www.list.am/')

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'menu'))
    )
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.LINK_TEXT, 'Տրանսպորտ')).perform()
    #driver.find_element(By.LINK_TEXT, 'Տրանսպորտ')
    driver.find_element(By.LINK_TEXT, 'Ավտոմեքենաներ').click()
    select = Select(driver.find_element(By.ID, 'crc'))
    select.select_by_value('0')
    driver.find_element(By.ID, 'idprice1').send_keys('1000')
    driver.find_element(By.ID, 'idprice2').send_keys('5000') #while entering for example '1000' and '5000' an error occurs
    driver.find_element(By.XPATH, "//input[@id='idprice2']/following::a[@class='btn']").click()
    
#    An jan you get error because when element2 does not exist, system wait 10 seconds and
#  return timeout exception. You can use try except in this case. If element2 will ve exist 
#  'No Result Found' will be printed, in other case ecept block will be executed
   
    try:
        element2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'notfound'))
        )
        print('No Result Found')
    except:
        print('Result Found')
        print(driver.current_url)
        driver.close()
except:
    print('Something went wrong')
finally:
    driver.quit()

print('Selenium forth task test case successfully completed')