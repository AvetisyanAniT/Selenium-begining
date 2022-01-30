
import pytest
from Duck.Duck.Pages.Base_page import TestBase
from Duck.Duck.Pages.search import TestDuckDuckGoSearchPage
from Duck.Duck.Pages.result import TestDuckDuckGoResultPage



#Activate Chrome browser
browser = TestBase().test_browser()

# Set up test case data
PHRASE = 'panda'

# Search for the phrase
search_page = TestDuckDuckGoSearchPage(browser)
search_page.test_load()
search_page.test_search(PHRASE)


# Verify that results appear
result_page = TestDuckDuckGoResultPage(browser)
assert result_page.test_link_div_count() > 0
assert result_page.test_phrase_result_count(PHRASE) > 0
assert result_page.test_search_input_value()==PHRASE

#Close browser
browser.close()