from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys 
 
print("sample test case started")  
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')  
# driver = webdriver.Firefox()
driver.maximize_window()  
#navigate to the url  
driver.get("https://www.google.com/")  

#identify the Google search text box and enter the value  
driver.find_element_by_name("q").send_keys("javatpoint")  
time.sleep(3)  

#click on the Google search button  
driver.find_element_by_name("btn").send_keys(Keys.ENTER)  
time.sleep(3)  

#close the browser  
driver.close()  
# print("sample test case successfully completed")  