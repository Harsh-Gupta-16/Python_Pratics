from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import time
val = ['0','1','2','3','4','5','6','7','8','9','10']
val2 = ['11','12','13','14','15','16']
bs=[]
pkg=[]
pric=[]
browser = webdriver.Chrome("E:\\Pyhton_Pratics\\driver\\chromedriver.exe")
browser.get("https://www.ebay.co.uk/itm/362473146146?hash=item5465154722:g:36oAAOSwOYRb1wn9")

# selecting Bolt Size
for boltsze in val:
    #time.sleep(10)
    boltsize = Select(browser.find_element_by_id('msku-sel-1')).select_by_value(boltsze)
    
    
    #selecting Package Quntity
    for pkgq in val2:
        pkgquality = Select(browser.find_element_by_id('msku-sel-2')).select_by_value(pkgq)
        #time.sleep(5)

        # Fetching the Price result
        price = browser.find_element_by_id('prcIsum').text
        print(price)
        bs.append(browser.find_element_by_id("msku-opt-" + boltsze).text)
        pkg.append(int(browser.find_element_by_id("msku-opt-" + pkgq).text))
        pric.append(price)

browser.close()

# Create the Header of the file
df = pd.DataFrame({'Bolt Size':bs,'Pack Quantity':pkg,'Price(Euro)':pric})
# exporting the excel File
df.to_excel('Bolt_Price_list2.xls', index=False)
