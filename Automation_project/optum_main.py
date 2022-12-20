# Import Packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome Driver Initialization
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
chrome_driver = "C:\\Users\\Harsh.x.Gupta\\Documents\\Automation\\drivers\\chromedriver.exe"

# Set Date Range
d1 = 2
d2 = 3
d3 = 2020
d1 = str(d1)
d2 = str(d2)
d3 = str(d3)
d4 = d1+"/"+d2+"/"+d3
print(d4)

driver = webdriver.Chrome(chrome_driver, options=options)

driver.find_element_by_id('tabDataFiles').click()


# Function to add payers to the bundle

def add_payers_14(driver_name):
    driver_name.find_element_by_xpath("//option[contains(.,'UHC Community Plan New Jersey')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver_name.find_element_by_xpath("//option[contains(.,'COVID19 HRSA Uninsured ')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver_name.find_element_by_xpath("//option[contains(.,'UHC Community Plan Michigan')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver_name.find_element_by_xpath("//option[contains(.,'UHC Community Plan of the Midlands')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of AZ')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of TX LLC')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of DE OBH')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'Golden Rule')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'Optum IOA program')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'AARP Supplemental Health Plans insured')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[@value='391995276']").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare Life Insurance Company')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of NY')]").click()
    driver.find_element_by_id("addBtn").click()

    # driver.find_element_by_id("submitBtn").click()

    return 0


# Function to 13 add payers to the bundle

def add_payers_13(driver_name):
    driver_name.find_element_by_xpath("//option[contains(.,'UHC Community Plan New Jersey')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver_name.find_element_by_xpath("//option[contains(.,'COVID19 HRSA Uninsured ')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver_name.find_element_by_xpath("//option[contains(.,'UHC Community Plan Michigan')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver_name.find_element_by_xpath("//option[contains(.,'UHC Community Plan of the Midlands')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of AZ')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of TX LLC')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of DE OBH')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'Golden Rule')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'Optum IOA program')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'AARP Supplemental Health Plans insured')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare Life Insurance Company')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of NY')]").click()
    driver.find_element_by_id("addBtn").click()

    # driver.find_element_by_id("submitBtn").click()

    return 0


# Function to add 8 payers to the bundle

def add_payers_8(driver_name):
    driver_name.find_element_by_xpath("//option[contains(.,'COVID19 HRSA Uninsured ')]").click()
    driver_name.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'Golden Rule')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'Optum IOA program')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'AARP Supplemental Health Plans insured')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[@value='391995276']").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UnitedHealthcare Life Insurance Company')]").click()
    driver.find_element_by_id("addBtn").click()

    driver.find_element_by_xpath("//option[contains(.,'UHC Community Plan of NY')]").click()
    driver.find_element_by_id("addBtn").click()

    # driver.find_element_by_id("submitBtn").click()

    return 0


# Creating Bundle for Tax ID 381882750
driver.find_element_by_id("taxIndNbrId").send_keys("952701802")
driver.implicitly_wait(10)
driver.find_element_by_name("fileTypes").click()
driver.implicitly_wait(10)

# Select Data Range
driver.find_element_by_name("settlementDateFrom").send_keys(d4)
driver.find_element_by_name("settlementDateTo").send_keys(d4)

# Call function to add Payers to bundle
add_payers_14(driver)
