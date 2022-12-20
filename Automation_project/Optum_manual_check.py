import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

payer_fourteen = ['381882750', '431039532', '161387862', '710897031', '952701802', '232933949', '232773941',
                  '364257926', '223137283', '251533746', '200310967', '880099333', '540854787', '352014838']

payer_eight = ['61460613', '731560760', '43248020', '520890739']
payer_nine = '461491586'
payer_thirteen = '382084239'


def wait():
    time.sleep(5)


# Function to add payers to the bundle

def add_payers_14():
    select = Select(browser.find_element_by_id('availablePayerTinNbrs'))
    select.select_by_value('223368602')  # UHC Community Plan New Jersey
    select.select_by_value('520821668')  # COVID19 HRSA Uninsured Treatment Fund
    select.select_by_value('383204052')  # UHC Community Plan Michigan
    select.select_by_value('470676824')  # UHC Community Plan of the Midlands
    select.select_by_value('860813232')  # UHC Community Plan of AZ
    select.select_by_value('912008361')  # UHC Community Plan of TX LLC
    select.select_by_value('942649097')  # UHC Community Plan of DE OBH
    select.select_by_value('376028756')  # Golden rule
    select.select_by_value('411289245')  # Unitedhealthcare
    select.select_by_value('411858498')  # Optum PAF Program
    select.select_by_value('362739571')  # AARP Supplemental Health plans insured by United Healthcare
    select.select_by_value('391995276')  # UMR
    select.select_by_value('860207231')  # United Healthcare  Life Insurance Company
    select.select_by_value('061172891')  # UHC Community Plan of NY
    wait()
    # click on add button
    browser.find_element_by_id('addBtn').click()

    #  click on submit button
    # driver_name.find_element_by_id("submitBtn").click()


def add_payer_13():
    select = Select(browser.find_element_by_id('availablePayerTinNbrs'))
    select.select_by_value('223368602')  # UHC Community Plan New Jersey
    select.select_by_value('520821668')  # COVID19 HRSA Uninsured Treatment Fund
    select.select_by_value('383204052')  # UHC Community Plan Michigan
    select.select_by_value('470676824')  # UHC Community Plan of the Midlands
    select.select_by_value('860813232')  # UHC Community Plan of AZ
    select.select_by_value('912008361')  # UHC Community Plan of TX LLC
    select.select_by_value('942649097')  # UHC Community Plan of DE OBH
    select.select_by_value('376028756')  # Golden rule
    select.select_by_value('411289245')  # Unitedhealthcare
    select.select_by_value('411858498')  # Optum PAF Program
    select.select_by_value('362739571')  # AARP Supplemental Health plans insured by United Healthcare
    select.select_by_value('860207231')  # United Healthcare  Life Insurance Company
    select.select_by_value('061172891')  # UHC Community Plan of NY

    # click on add button
    browser.find_element_by_id('addBtn').click()

    #  click on submit button
    # driver_name.find_element_by_id("submitBtn").click()


def add_payer_9():
    select = Select(browser.find_element_by_id('availablePayerTinNbrs'))
    select.select_by_value('520821668')  # COVID19 HRSA Uninsured Treatment Fund
    select.select_by_value('376028756')  # Golden rule
    select.select_by_value('411289245')  # Unitedhealthcare
    select.select_by_value('411858498')  # Optum PAF Program
    select.select_by_value('362739571')  # AARP Supplemental Health plans insured by United Healthcare
    select.select_by_value('391995276')  # UMR
    select.select_by_value('860207231')  # United Healthcare  Life Insurance Company
    select.select_by_value('043149694')  # Harvard Pilgrim
    select.select_by_value('061172891')  # UHC Community Plan of NY

    # click on add button
    browser.find_element_by_id('addBtn').click()

    #  click on submit button
    # browser.find_element_by_id("submitBtn").click()


def add_payer_8():
    select = Select(browser.find_element_by_id('availablePayerTinNbrs'))
    select.select_by_value('520821668')  # COVID19 HRSA Uninsured Treatment Fund
    select.select_by_value('376028756')  # Golden rule
    select.select_by_value('411289245')  # Unitedhealthcare
    select.select_by_value('411858498')  # Optum PAF Program
    select.select_by_value('362739571')  # AARP Supplemental Health plans insured by United Healthcare
    select.select_by_value('391995276')  # UMR
    select.select_by_value('860207231')  # United Healthcare  Life Insurance Company
    select.select_by_value('061172891')  # UHC Community Plan of NY

    # click on add button
    browser.find_element_by_id('addBtn').click()

    #  click on submit button
    # browser.find_element_by_id("submitBtn").click()


# creating time stamp
dateTimeObj = datetime.datetime

# Set date for automatic
fromdate = dateTimeObj.now().strftime("%m/01/%Y")
todate = (dateTimeObj.now() - datetime.timedelta(days=1)).strftime("%m/%d/%Y")

# Calling browser for work
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
# chrome.exe --remote-debugging-port=9222
# chrome.exe --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir="C:\remotedebugfolder"
#
# Manohar.X.Samuel@questdiagnostics.com
# Temporary11
browser = webdriver.Chrome("C:\\Users\\Harsh.x.Gupta\\Documents\\Automation\\drivers\\chromedriver.exe",
                           options=options)

# Creating Bundle for Tax ID 952701802
browser.find_element_by_id("taxIndNbrId").send_keys("952701802")
wait()
browser.find_element_by_xpath('//*[@id="835Checkbox"]/input').click()
# Select Data Range
browser.find_element_by_name("settlementDateFrom").send_keys(todate)
wait()
browser.find_element_by_name("settlementDateTo").send_keys(todate)

# Call function to add Payers to bundle
add_payers_14()
