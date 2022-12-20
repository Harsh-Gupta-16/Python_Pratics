#Purpose: Downloading all the Default report
# Version 1
# Developer: Harsh Gupta

from selenium import webdriver


browser = webdriver.Chrome("C:\\Billing_RL\\drivers\\chromedriver")
browser.get("http://qdcws3206.us.qdx.com/billingteam3/")
browser.implicitly_wait(10)
# selecting the Resource Base Report
browser.find_element_by_xpath('''//*[@id="ctl00_NavigationMenun2"]/td/table/tbody/tr/td/a''').click()
browser.implicitly_wait(10)
# selecting all the resources
browser.find_element_by_id('ctl00_MainContent_chkAll').click()
# selecting all the activity type
browser.find_element_by_id('ctl00_MainContent_CheckBox1').click()
# selecting the timming
browser.find_element_by_id('ctl00_MainContent_CheckBoxList3_0').click()
browser.find_element_by_id('ctl00_MainContent_CheckBoxList3_1').click()
#entering the from date in US standard MM/DD/YYYY
browser.find_element_by_id('ctl00_MainContent_datepicker').send_keys('04/01/2021')
#entering the to date in US standard MM/DD/YYYY
browser.find_element_by_id('ctl00_MainContent_TextBox1').send_keys('04/04/2021')
browser.implicitly_wait(5)
# clicking on Genrating report
browser.find_element_by_id('ctl00_MainContent_Button1').click()
# download the genrated report
browser.find_element_by_id('ctl00_MainContent_ImageButton1').click()