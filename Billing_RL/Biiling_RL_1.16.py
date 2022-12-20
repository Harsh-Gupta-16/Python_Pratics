# Purpose: Downloading all the Default report
# Version 1.16 Removing Email Functionality
# Developer: Harsh Gupta

# importing package
import glob
import os
import time
import datetime
import smtplib
import getpass
import xlwt
import pandas as pd
from email.message import EmailMessage
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client as win32

# creating variable
effor, Resourc, Applicatio, Activit, Sub_Activit, Descriptio, Effort_Hour, Timing = [], [], [], [], [], [], [], []
incomplete_file = 'None'
wait, wait1 = True, True
links = ["http://qdcws3206.us.qdx.com/billingteam1/ReportByName.aspx",
         "http://qdcws3206.us.qdx.com/billingteam2/ReportByName.aspx",
         "http://qdcws3206.us.qdx.com/billingteam3/ReportByName.aspx",
         "http://qdcws3206.us.qdx.com/billingteam4/ReportByName.aspx",
         "http://10.43.8.164/ResourceUtilizationBillingone/ReportByName.aspx",
         "http://10.43.8.164/ResourceUtilizationBillingTwo/ReportByName.aspx",
         "http://10.43.8.164/ResourceUtilizationBillingThree/ReportByName.aspx",
         "http://10.43.8.164/ResourceUtilizationBillingFour/ReportByName.aspx"]

# User input from user
fromdate = str(input('Enter the from Date in MM/DD/YYYY: '))
todate = str(input('Enter the to Date in MM/DD/YYYY: '))
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
    browser.find_element_by_id('ctl00_MainContent_ImageButton1').click()


print('Start downloading the report file')
# calling the offsite billing url
for link in links:
    browser.get(link)
    browser.implicitly_wait(10)
    generate_report()
    browser.implicitly_wait(20)

# waiting
time.sleep(15)

# Checking the download file is completed for not
# checking crdownlaod
while wait:
    for filename in os.listdir(os.environ.get('userprofile') + '\\Downloads'):
        if filename.endswith('crdownload'):
            incomplete_file = filename
    if os.path.exists(os.environ.get('userprofile') + '\\Downloads\\' + incomplete_file):
        time.sleep(15)
    else:
        wait = False
    # checking tmp
while wait1:
    for filename in os.listdir(os.environ.get('userprofile') + '\\Downloads'):
        if filename.endswith('tmp'):
            incomplete_file = filename
    if os.path.exists(os.environ.get('userprofile') + '\\Downloads\\' + incomplete_file):
        time.sleep(15)
    else:
        wait1 = False

# checking crdownlaod for download one drive folder
while wait2:
    for filename in os.listdir(os.environ.get('userprofile') + '\\OneDrive - Quest Diagnostics\\Downloads'):
        if filename.endswith('crdownload'):
            incomplete_file = filename
    if os.path.exists(os.environ.get('userprofile') + '\\OneDrive - Quest Diagnostics\\Downloads\\' + incomplete_file):
        time.sleep(15)
    else:
        wait2 = False
    # checking tmp
while wait3:
    for filename in os.listdir(os.environ.get('userprofile') + '\\OneDrive - Quest Diagnostics\\Downloads'):
        if filename.endswith('tmp'):
            incomplete_file = filename
    if os.path.exists(os.environ.get('userprofile') + '\\OneDrive - Quest Diagnostics\\Downloads\\' + incomplete_file):
        time.sleep(15)
    else:
        wait3 = False

# closing browser
browser.quit()

print('Downloading of file Completed')

# Checking the inprogress folder empty or not
cmd = 'if exist *.* ( del C:\\Billing_RL\\inprogress\\*.x* )'
os.system(cmd)

print('Moving the file to inprogress Folder')
# Moving the download file to specific location
# getting userprofile location
user = os.environ.get('userprofile')
# Checking and Moving the file from download location to specific location
cmd = 'if exist ' + user + '\\downloads\\Tracker*.xls ( move ' + user + '\\downloads\\Tracker*xls C:\\Billing_RL\\inprogress )'
os.system(cmd)

# Checking and Moving the file from One Drive download location to specific location
user = os.environ.get('userprofile') + '\\' + '"OneDrive - Quest Diagnostics"'
cmd = 'if exist ' + user + '\\downloads\\Tracker*.xls ( move ' + user + '\\downloads\\Tracker*xls C:\\Billing_RL\\inprogress)'
os.system(cmd)

# waiting
time.sleep(15)

print('Moving of file Completed')
print('Start Merging of file')

# Merging the downloaded files
read_files = glob.glob('Tracker*.xls')
with open("defaulter_list.tmp1", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

# Removing the downloaded files
for del_file in read_files:
    os.remove(del_file)

# Creating the new merging excel file
# open the merge file
content = open("defaulter_list.tmp1", "r")
soup = BeautifulSoup(content, features="lxml")
# find the table row tag i.e 'tr' from the merge file

rows = soup.find_all('tr')
for row in rows:
    # fetching the data from table data tag i.e 'td'
    # effor.append(row.find_next('td').text)
    effor.append((dateTimeObj.strptime(row.find_next('td').text, '%m/%d/%Y')).date())
    Resourc.append(row.find_next('td').find_next('td').text)
    Applicatio.append(row.find_next('td').find_next('td').find_next('td').text.strip())
    Activit.append(row.find_next('td').find_next('td').find_next('td').find_next('td').text.strip())
    Sub_Activit.append(row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip())
    Descriptio.append(row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next(
        'td').text.strip())
    Effort_Hour.append(float(
        row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next(
            'td').text.strip()))
    Timing.append(
        row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next(
            'td').find_next('td').text.strip())

# Creating the Header of the file
df = pd.DataFrame(
    {'Effort': effor, 'Resource': Resourc, 'Application': Applicatio, 'Activity': Activit, 'Sub Activity': Sub_Activit,
     'Description': Descriptio, 'Effort Hours': Effort_Hour, 'Timings': Timing})
# exporting the final file
df.to_excel('RL.xls', index=False)
time.sleep(5)

# Closing of content file
content.close()

print('Merging has been Completed')
# print('Merger File Name: ' + file_name)

# removing the tmp1 file
for del_file in glob.glob('*.tmp1'):
    os.remove(del_file)

# Copy RL_template to inprogress
cmd = 'copy C:\\Billing_RL\\template\\RL_Defaulter_Template.xlsm C:\\Billing_RL\\inprogress'
os.system(cmd)

# Calling Macro
xl = win32.Dispatch('Excel.Application')
xl.Application.visible = False  # change to True if you are desired to make Excel visible
wb = xl.Workbooks.Open("c:\\Billing_RL\\inprogress\\RL_Defaulter_Template.xlsm")
xl.Application.run("RL_Defaulter_Template.xlsm!Module1.DEFAULTER")
wb.Save()
wb.Close()
xl.Application.Quit()
del xl

# rename defaulter list to new filename
# cmd = 'rename Resource_Loading_Defaulter.xls ' + file_name
# os.system(cmd)

# print('Start sending the mail to ' + receiver)

# sending file via mail
# server = smtplib.SMTP('smtp.office365.com', 587)
# server.starttls()
# server.login(sender, sender_passwd)
# email = EmailMessage()
# email['From'] = sender
# email['To'] = receiver
# email['Subject'] = 'Billing Resource loading For Default from ' + fromdate + ' to ' + todate
# email.set_content('''Please find the attached document for the Billing Resource location\n\n File Name :''' + file_name)
# with open(file_name, 'rb') as fp:
#     exl_read = fp.read()
# email.add_attachment(exl_read, maintype='application',
#                      subtype='vnd.ms-excel',
#                      filename=file_name)
# server.send_message(email)
# print('Mail has been sent')

# Archiving the file
# print('Archiving the sent file')
# cmd = 'move Billing_Resource_loading_*xls C:\\Billing_RL\\Archive'
# os.system(cmd)
# print('Archiving of file has been Completed')
