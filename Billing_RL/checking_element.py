# Purpose: Downloading all the Default report
# Version 1.16 Removing Email Functionality
# Developer: Harsh Gupta

import datetime
# importing package
import time

from selenium import webdriver

# creating variable
effor, Resourc, Applicatio, Activit, Sub_Activit, Descriptio, Effort_Hour, Timing = [], [], [], [], [], [], [], []
incomplete_file = 'None'
wait, wait1 = True, True
links = ["http://clvwd22006h8/resourceutilizationwebmisc/ReportByName.aspx",
         "http://qdcws3206.us.qdx.com/billingteam4/ReportByName.aspx"]

# User input from user
fromdate = '04/02/2021'
todate = '04/09/2021'
# sender = str(input('Enter the Sender Mail ID: '))
# sender_passwd = getpass.getpass(prompt='Enter the Email id password: ')
# receiver = str(input('Enter the Receiver Mail ID: '))

# creating time stamp
dateTimeObj = datetime.datetime
timestamp = dateTimeObj.now().strftime("%d%m%Y_%H%M%S")

# Creating the file name
file_name: str = 'Billing_Resource_loading_Defaulter' + timestamp + '.xls'

# calling driver
browser = webdriver.Chrome("C:\\Billing_RL\\drivers\\chromedriver")


# Create Generate Report Function

def generate_report():
    # selecting the Resource Base Report
    browser.implicitly_wait(10)
    # selecting all the resources
    browser.find_element_by_id('ctl00_MainContent_chkAll').click()
    # selecting all the activity type
    browser.find_element_by_id('ctl00_MainContent_CheckBox1').click()
    # selecting the timing
    browser.find_element_by_id('ctl00_MainContent_CheckBoxList3_0').click()
    browser.find_element_by_id('ctl00_MainContent_CheckBoxList3_1').click()
    # entering the from date in US standard MM/DD/YYYY
    browser.find_element_by_id('ctl00_MainContent_datepicker').send_keys(fromdate)
    # entering the to date in US standard MM/DD/YYYY
    browser.find_element_by_id('ctl00_MainContent_TextBox1').send_keys(todate)
    browser.implicitly_wait(5)
    # clicking on Generating report
    browser.find_element_by_id('ctl00_MainContent_Button1').click()
    # download the generated report
    try:
        browser.find_element_by_id('ctl00_MainContent_ImageButton1').click()
    except:
        pass
    # browser.find_element_by_id('ctl00_MainContent_ImageButton1').click()
    # if (browser.find_element_by_id('ctl00_MainContent_ImageButton1')).size() > 0:
    #     print('found')
    # else:
    #     print('not found')


#

print('Start downloading the report file')
# calling the offsite billing url
for link in links:
    browser.get(link)
    browser.implicitly_wait(10)
    generate_report()
    browser.implicitly_wait(20)

# waiting
time.sleep(15)

# closing browser
# browser.quit()

print('Downloading of file Completed')
