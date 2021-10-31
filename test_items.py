#"236895", "236896","236897","236898","236899","236903","236904","236905"
import pytest
import time
import math
from selenium import webdriver



def test_guest_should_see_login_link(browser):

  
    if browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket"):
        print('this button exists on the site')
        assert True
    else:
        print('this button does not exist on the site')
        assert False



    
    