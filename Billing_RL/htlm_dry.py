import pandas as pd
from bs4 import BeautifulSoup
import xlwt
# effor,Resourc,Applicatio,Activit,Sub_Activit,Descriptio,Effort_Hour,Timing=([], )*8
values=[]
Resourc=[]
Applicatio=[]
content = open('b.html','r')
soup = BeautifulSoup(content,features="html.parser")
div = soup.find("div")
values = []

for tr in div.find_all('tr'):
    values.append(tr.find("td").text)

print(values)
    
    