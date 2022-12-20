# Purpose: Downloading all the Default report
# Version 1.9 - moving the file to specific location
# Developer: Harsh Gupta

# importing package
import glob
import os
import time
import datetime
import smtplib
import xlwt
import pandas as pd
from email.message import EmailMessage
from selenium import webdriver
from bs4 import BeautifulSoup

# creating variable
effor, Resourc, Applicatio, Activit, Sub_Activit, Descriptio, Effort_Hour, Timing = [], [], [], [], [], [], [], []
incomplete_file = 'None'
wait, wait1 = True, True
links = ["http://qdcws3206.us.qdx.com/billingteam1/", "http://qdcws3206.us.qdx.com/billingteam2/",
         "http://qdcws3206.us.qdx.com/billingteam3/", "http://qdcws3206.us.qdx.com/billingteam4/"]

# User input from user
fromdate = str(input('Enter the from Date in MM/DD/YYYY: '))
todate = str(input('Enter the to Date in MM/DD/YYYY: '))
# creating time stamp
dateTimeObj = datetime.datetime
timestamp = dateTimeObj.now().strftime("%d%m%Y_%H%M%S")

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
    # entering the from date in US standard MM/DD/YYYY
    browser.find_element_by_id('ctl00_MainContent_datepicker').send_keys(fromdate)
    # entering the to date in US standard MM/DD/YYYY
    browser.find_element_by_id('ctl00_MainContent_TextBox1').send_keys(todate)
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
    browser.implicitly_wait(20)

# waiting
time.sleep(15)

# Checking the download file is completed for not
# checking crdownlaod
while wait:
    for filename in os.listdir('.'):
        if filename.endswith('crdownload'):
            incomplete_file = filename
    if os.path.exists(incomplete_file):
        time.sleep(15)
    else:
        wait = False
    # checking tmp
while wait1:
    for filename in os.listdir('.'):
        if filename.endswith('tmp'):
            incomplete_file = filename
    if os.path.exists(incomplete_file):
        time.sleep(15)
    else:
        wait1 = False

# closing browser
browser.quit()

# Moving the download file to specific location
# getting userprofile location
user = os.environ.get('userprofile')
# Checking and Moving the file from download location to specific location
cmd = 'if exist ' + user + '\\downloads\\*.xls ( move ' + user + '\\downloads\\*xls C:\\Billing_RL\\inprogress )'
os.system(cmd)

# Checking and Moving the file from One Drive download location to specific location
user = os.environ.get('userprofile') + '\\' + '"OneDrive - Quest Diagnostics"'
cmd = 'if exist ' + user + '\\downloads\\*.xls ( move ' + user + '\\downloads\\*xls C:\\Billing_RL\\inprogress)'
os.system(cmd)

# waiting
time.sleep(15)

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
# Creating the file name
file_name: str = 'Billing_Resource_loading_' + timestamp + '.xls'
# exporting the final file
df.to_excel(file_name, index=False)
time.sleep(5)

# Closing of content file
content.close()

# removing the tmp1 file
for del_file in glob.glob('*.tmp1'):
    os.remove(del_file)

# sending file via mail
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login('Harsh.x.Gupta@questdiagnostics.com', 'Welcome22')
email = EmailMessage()
email['From'] = 'Harsh.x.Gupta@questdiagnostics.com'
email['To'] = 'Harsh.x.Gupta@questdiagnostics.com'
email['Subject'] = 'Billing Resource loading from ' + fromdate + ' to ' + todate
email.set_content('''Please find the attached document for the Billing Resource location\n\n File Name :''' + file_name)
with open(file_name, 'rb') as fp:
    exl_read = fp.read()
email.add_attachment(exl_read, maintype='application',
                     subtype='vnd.ms-excel',
                     filename=file_name)
server.send_message(email)
