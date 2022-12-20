from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import time
val1 = ['0','1','2','3','4','5']
val2=['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
val3 = ['26','27','28','29']
thr= []
bs =[]
pkg=[]
pric=[]
browser = webdriver.Chrome("E:\\Python_Pratics\\driver\\chromedriver.exe")
browser.get("https://www.ebay.co.uk/itm/181083513195?hash=item2a296b216b:g:JCQAAOSw9j9dkwUq")
# boltsize = Select(browser.find_element_by_id('msku-sel-1')).select_by_value(0)
# pkgquality = Select(browser.find_element_by_id('msku-sel-2')).select_by_value('26')
# price = browser.find_element_by_id('prcIsum').text
# print(price)
# browser.close()

# selecting Bolt Size
for thresh in val1:
    # time.sleep(3)
    Select(browser.find_element_by_id('msku-sel-2')).select_by_value('-1')
    Select(browser.find_element_by_id('msku-sel-3')).select_by_value('-1')
    thres = Select(browser.find_element_by_id('msku-sel-1')).select_by_value(thresh)
    # thr.append(str(browser.find_element_by_id("msku-opt-" + thresh).text))

    for boltsze in val2:
        # time.sleep(3)
        try:
            # Select(browser.find_element_by_id('msku-sel-2')).select_by_value('-1')
            # time.sleep(2)
            boltsize = Select(browser.find_element_by_id('msku-sel-2')).select_by_value(boltsze)
            # bs.append(browser.find_element_by_id("msku-opt-" + boltsze).text)
            # print(browser.find_element_by_id("msku-opt-" + boltsze).text)
        except:
            continue
        for pkgq in val3:
            try:
                # time.sleep(3)
                pkgquality = Select(browser.find_element_by_id('msku-sel-3')).select_by_value(pkgq)
                price = browser.find_element_by_id('prcIsum').text
                Select(browser.find_element_by_id('msku-sel-3')).select_by_value('-1')
                print(price)
                thr.append(browser.find_element_by_id("msku-opt-" + thresh).text)
                bs.append(browser.find_element_by_id("msku-opt-" + boltsze).text)
                pkg.append(int(browser.find_element_by_id("msku-opt-" + pkgq).text))
                pric.append(price)
            except:
                continue    

browser.close()
print(thr)
print(bs)
print(pkg)
print(pric)
# Create the Header of the file
df = pd.DataFrame({'Thread  Size':thr,'Bolt Size':bs,'Pack Quantity':pkg,'Price(Euro)':pric})
# exporting the excel File
df.to_excel('Bolt_Price_list.xls', index=False)
