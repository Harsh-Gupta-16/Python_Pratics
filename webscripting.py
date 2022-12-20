from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import time
val = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
val2 = ['25','26','27','28','29','30']
bs=[]
pkg=[]
pric=[]
browser = webdriver.Chrome("E:\\Python_Pratics\\driver\\chromedriver.exe")
browser.get("https://www.ebay.co.uk/itm/181229357040?hash=item2a321c87f0:g:DbcAAOxy-W9SSn9Z")
# boltsize = Select(browser.find_element_by_id('msku-sel-1')).select_by_value(0)
# pkgquality = Select(browser.find_element_by_id('msku-sel-2')).select_by_value('26')
# price = browser.find_element_by_id('prcIsum').text
# print(price)
# browser.close()

# selecting Bolt Size
for boltsze in val:
    time.sleep(10)
    # count = 0
    boltsize = Select(browser.find_element_by_id('msku-sel-1')).select_by_value(boltsze)
    # print(browser.find_element_by_id("msku-opt-" + '%01d' % count).text)
    # print(browser.find_element_by_id("msku-opt-" + boltsze).text)
    
    #selecting Package Quntity
    for pkgq in val2:
        pkgquality = Select(browser.find_element_by_id('msku-sel-2')).select_by_value(pkgq)
        time.sleep(5)

        # Fetching the Price result
        price = browser.find_element_by_id('prcIsum').text
        # print(price)
        bs.append(browser.find_element_by_id("msku-opt-" + boltsze).text)
        pkg.append(int(browser.find_element_by_id("msku-opt-" + pkgq).text))
        pric.append(price)

# print(bs)
# print(pkg)
# print(pric)
browser.close()
# Create the Header of the file
df = pd.DataFrame({'Bolt Size':bs,'Pack Quantity':pkg,'Price(Euro)':pric})
# exporting the excel File
df.to_excel('Bolt_Price_list.xls', index=False)
