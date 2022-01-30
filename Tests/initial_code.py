# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# def test_basic_duckduckgo_search():
#     URL = 'https://www.duckduckgo.com'
#     PHRASE = 'panda'

#     browser = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
#     browser.get(URL)

#     search_input = browser.find_element_by_id('search_form_input_homepage')
#     search_input.send_keys(PHRASE + Keys.RETURN)

#     link_divs = browser.find_elements_by_css_selector('#links > div')
#     assert len(link_divs) > 0

#     xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
#     results = browser.find_elements_by_xpath(xpath)
#     assert len(results) > 0

#     search_input = browser.find_element_by_id('search_form_input')
#     assert search_input.get_attribute('value') == PHRASE

# test_basic_duckduckgo_search()

import sys

# sys.path.append('C:\\Anna\\Automation\\selenium\\Lesson_20')
print(sys.path)