import pandas as pd
from bs4 import BeautifulSoup 
import xlwt
effor,Resourc,Applicatio,Activit,Sub_Activit,Descriptio,Effort_Hour,Timing=[],[],[],[],[],[],[],[]
# effor=[]
# Resourc=[]
# Applicatio=[]
content = open('b.html','r')
soup = BeautifulSoup(content,features="lxml")
rows = soup.find_all('tr')
for row in rows:
    # effort=row.find_next('td').text.strip()
    # Resource=row.find_next('td').find_next('td').text.strip()
    # Application=row.find_next('td').find_next('td').find_next('td').text.strip()
    # Activity=row.find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    # Sub_Activity=row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    # Description=row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    # Effort_Hours=row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    # Timings=row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    # print(effort,Resource,Application,Activity,Sub_Activity,Effort_Hours,Timings)
    effor.append(row.find_next('td').text)
    Resourc.append(row.find_next('td').find_next('td').text)
    Applicatio.append(row.find_next('td').find_next('td').find_next('td').text.strip())
    # Activit.append(row.find_next('td').find_next('td').find_next('td').find_next('td').text.strip())
    # Sub_Activit.append(row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip())
    # Descriptio.append(row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip())
    # Effort_Hour.append(row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip())
    Timing.append(row.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip())

df = pd.DataFrame({'Product Name':effor,'Price':Resourc,'Rating':Timing}) 
df.to_excel('products.xls', index=False, encoding='utf-8',)