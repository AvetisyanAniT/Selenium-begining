from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re

print('Selenium third task test case started')
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.list.am/')

def maxPrice():
    driver.find_element_by_link_text('Անշարժ գույք').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Բնակարաններ').send_keys(Keys.ENTER)
    time.sleep(1)
    elems=[]
    elems = driver.find_elements_by_xpath("//div[@class='gl']/a/child::div[@class='p']")
    price_list=[]
    for i in range(5):
        price = elems[i].text
        priceNum = re.findall('\d+', price)[0]
        # Anna-An jan i extracted only numbers, because in case when price currency AMD, 
        # your regular expression does not  replace it
        priceInt = int(priceNum)
        price_list.append(priceInt)
        #Anna- Here you try get max from integer, that's why you got error
    return max(price_list) 
#max function isn't working
print(maxPrice())
driver.close()

print('Selenium third task test case successfully completed')