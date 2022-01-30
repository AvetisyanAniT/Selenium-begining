from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def test_check_the_radiobutton_text():
    print('Selenium fifth task test case started')

    URL = 'https://www.seleniumeasy.com/test/'
    WORD = 'Male'

    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')
    driver.maximize_window()

    # Navigate to webpage https://www.seleniumeasy.com/test/
    driver.get(URL)

    try:
        # Close opened popup, if popup exist
        try:
            popup = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'at-cv-lightbox-header'))
            )
            driver.find_element(By.ID, 'at-cv-lightbox-close').click()
        except:
            print('No popup displayed')

        # Scroll to Menu List
        treemenu = driver.find_element(By.ID, 'treemenu')
        driver.execute_script('arguments[0].scrollIntoView();', treemenu)

        # Click on "Radio buttons Demo"
        driver.find_element(By.LINK_TEXT, 'Input Forms').click()
        driver.find_element(By.LINK_TEXT, 'Radio Buttons Demo').click()

        # Choose Male Radiobutton under "Radio Button Demo" section
        driver.find_element(By.XPATH, "//input[@value = 'Male' and @name = 'optradio']").click()

        # Click Get check value button
        driver.find_element(By.ID, 'buttoncheck').click()

        # Check that Male word exist in message, if not, save screenshot
        text = driver.find_element(By.CSS_SELECTOR, "p.radiobutton").text
        if WORD in text:
            pass
            # print('ok')
        else:
            # print('not ok')
            driver.save_screenshot("D:\QA Auto\lesson16\male_in_text.png")
    except:
        print('Something went wrong')
    finally:
        driver.quit()

    print('Selenium fifth task test case successfully completed')

test_check_the_radiobutton_text()
