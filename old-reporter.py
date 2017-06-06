from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import time

from . import secret

def wait(secs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            time.sleep(secs)
            return ret
        return wrapper
    return decorator

driver = webdriver.Chrome()
waiting = WebDriverWait(driver, 10)
driver.get('''https://clear.kaiserpermanente.org/#/retention-tool''')

elem1 = waiting.until(EC.element_to_be_clickable(('id','email')))

email = driver.find_element_by_id('email')
email.send_keys(username)

driver.implicitly_wait(5) # seconds

pw = driver.find_element_by_id('password')
pw.send_keys(password)

@wait(2)
def click_submit():
	driver.find_element_by_class_name('col-xs-5')
	elem2.click()



@wait(2)
def retention():
	elem4 = driver.find_element_by_id('retentionLink')
	elem4.click()

driver.implicitly_wait(5) # seconds

driver.implicitly_wait(10) # seconds

try:
    driver.switch_to_alert().accept()
except NoAlertPresentException as e: 
    driver.implicitly_wait(10)

try:
    driver.switch_to_alert().accept()
except NoAlertPresentException as e: 
    driver.implicitly_wait(10)

try:
    searchElem = driver.find_element_by_link_text('Current Business')
except NoAlertPresentException as e: 
    driver.switch_to_alert().accept()

# searchElem = driver.find_element_by_link_text('#ctl00_MainContent_maincontent_pfSearchMain_txtProviderName')
# searchElem.send_keys(provider_name)

driver.implicitly_wait(10) # seconds

searchElem = driver.find_element_by_link_text('Current Business')
elem.click()

# elem = driver.find_element_by_css_selector('''#btnSearch''')
# elem.click()

# driver.quit()