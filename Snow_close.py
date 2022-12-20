import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome("C:\\RL_automate\\drivers\\chromedriver")


# Create wait function
def wait():
    time.sleep(5)


# Open the service now website
browser.get('https://questprod.service-now.com/nav_to.do?uri=%2Fhome.do%3F')
wait()
browser.implicitly_wait(5)
# search the ticket number
browser.find_element_by_id('sysparm_search').send_keys('INC1058406' + '\n')
# select the state as close
Select(browser.find_element_by_id('incident.state')).select_by_value('8')
# select the resolution code
Select(browser.find_element_by_id('incident.close_code')).select_by_value()
# Enter the Resolution Note
browser.find_element_by_id('incident.close_notes').send_keys('False alert')

# Click on update
browser.find_element_by_id('sysverb_update_bottom').click()
wait()
