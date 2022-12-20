#Purpose: Downloading all the Default report
# Version 1.2 - Code enhancemnet
# Developer: Harsh Gupta

from selenium import webdriver

# creating variable
links=["http://qdcws3206.us.qdx.com/billingteam1/","http://qdcws3206.us.qdx.com/billingteam2/",
      "http://qdcws3206.us.qdx.com/billingteam3/","http://qdcws3206.us.qdx.com/billingteam4/"]
# calling driver
browser = webdriver.Chrome("C:\\Billing_RL\\drivers\\chromedriver")

# creating genrate report function
def generate_report():
    browser.find_element_by_xpath('''//*[@id="ctl00_NavigationMenun2"]/td/table/tbody/tr/td/a''').click()
    # selecting the Resource Base Report
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

# calling the billing url
for link in links:
    browser.get(link)
    browser.implicitly_wait(10)
    generate_report()
