import time
import sys
import csv
from selenium import webdriver
from selenium.webdriver.support.select import Select

count = 2
browser = webdriver.Chrome("C:\\RL_automate\\drivers\\chromedriver")


# Create wait function
def wait():
    time.sleep(5)


browser.get("http://qdcws3206.us.qdx.com/billingtower/")
wait()
Select(browser.find_element_by_id("ctl00_MainContent_DropDownList1")).select_by_value("117")
wait()
# Selecting the date
browser.find_element_by_xpath('//*[@title="' + sys.argv[1] + '"]').click()
wait()
with open('C:\\RL_automate\\Task.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)
    for row in csvReader:
        # Timing
        wait()
        if row['Timings'] == 'Office':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlTimings")).select_by_value("Office")
            # break
        else:
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlTimings")).select_by_value("Outside Office")
            # break
        # Tower
        wait()
        if row['Application'] == 'Billing EDI':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlApplication")).select_by_value("15")
            # break
        elif row['Application'] == 'Billing Web':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlApplication")).select_by_value("1")
        # Activity adn Sub activity
        if row['Activity'] == 'Production Support - IM activities':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_type")).select_by_value("1")
            wait()
            if row['SubActivity'] == 'IM activity':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1A")
            elif row['SubActivity'] == 'Customer meeting':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1B")
            elif row['SubActivity'] == 'Documentation':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1C")
            elif row['SubActivity'] == 'Knowledge Transition from Quest':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1D")
            elif row['SubActivity'] == 'PI Activity':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1E")
            elif row['SubActivity'] == 'Internal Meeting':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1F")
            elif row['SubActivity'] == 'Sev-9':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("1G")
            # break
        elif row['Activity'] == 'Production Support - Non IM activities':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_type")).select_by_value("2")
            wait()
            if row['SubActivity'] == 'Non IM activity':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("2A")
            elif row['SubActivity'] == 'Customer meeting':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("2B")
            elif row['SubActivity'] == 'Documentation':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("2C")
            elif row['SubActivity'] == 'Knowledge Transition from Quest':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("2D")
            elif row['SubActivity'] == 'PI Activity':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("2E")
            elif row['SubActivity'] == 'Internal Meeting':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("2F")
            # break
        elif row['Activity'] == 'Enhancements less than 80 hour':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_type")).select_by_value("3")
            wait()
            if row['SubActivity'] == 'Non IM activity':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3A")
            elif row['SubActivity'] == 'Enhancement':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3B")
            elif row['SubActivity'] == 'Customer meeting':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3C")
            elif row['SubActivity'] == 'Documentation':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3D")
            elif row['SubActivity'] == 'Knowledge Transition from Quest':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3E")
            elif row['SubActivity'] == 'PI Activity':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3F")
            elif row['SubActivity'] == 'Internal Meeting':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3F")
            elif row['SubActivity'] == 'Requirement Finalization':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3F")
            elif row['SubActivity'] == 'Analysis & Design':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3F")
            elif row['SubActivity'] == 'Coding':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("3F")
            # break
        elif row['Activity'] == 'Other':
            Select(browser.find_element_by_id(
                "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_type")).select_by_value("6")
            wait()
            if row['SubActivity'] == 'TCS internal Project Management':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("6A")
            elif row['SubActivity'] == 'TCS internal Training':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("6B")
            elif row['SubActivity'] == 'Self learning':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("6C")
            elif row['SubActivity'] == 'Leave':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("6D")
            elif row['SubActivity'] == 'Break':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("6E")
            elif row['SubActivity'] == 'TCS Internal IPMS/IQMS':
                Select(browser.find_element_by_id(
                    "ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ddlActivity_Subtype")).select_by_value("6F")
            # break
        # adding Description
        browser.find_element_by_id("ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_TextBox2").send_keys(
            row['Description'])
        # adding Time
        browser.find_element_by_id("ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_TextBox3").send_keys(
            row['Hours'])
        count = count + 1
        # adding new row
        if row['Complete'] == 'continue':
            browser.find_element_by_id("ctl00_MainContent_Gridview1_ctl" + '%02d' % count + "_ButtonAdd").click()
        else:
            break
        # end of ending task
    # end of For
# csv close
# Click on Save Button
browser.find_element_by_id("ctl00_MainContent_Button1").click()
# switch to Alert and Accept
aler = browser.switch_to.alert
aler.accept()
browser.quit()
