# Purpose: Downloading all the Default report
# Version 1.4 - Checking the download file is complete or not
# Developer: Harsh Gupta

# importing package
import glob
import os
import time
from selenium import webdriver



# creating variable
effor,Resourc,Applicatio,Activit,Sub_Activit,Descriptio,Effort_Hour,Timing=[],[],[],[],[],[],[],[]
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
    browser.implicitly_wait(10)

# Checking the download file is completed for not
incomplete_file = 'None'
wait = True
while(wait==True):
    for filename in os.listdir('.'):
        if filename.endswith('crdownload'):
            incomplete_file=filename
    if os.path.exists(incomplete_file):
        time.sleep(15)
    else:
        wait=False

# closing browser
browser.quit()

# Working with Execl files
read_files=glob.glob('Tracker*.xls')
with open("defaulter_list.tmp", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

# Removing the downloaded files
for delfile in read_files:
    os.remove(delfile)
