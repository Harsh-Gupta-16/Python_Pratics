import pyodbc
import pandas as pd

# Billing Tower connection
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws3206\D$\applications\billingtower\Resource_loading_Billing.mdb;')
# cursor = conn.cursor()
sql_query = pd.read_sql_query('select User_Name from Resource', conn)
df = pd.DataFrame(sql_query)
df['Tower'] = 'Billing'
df.to_csv(r'C:\Billing_RL\template\export_data.csv', index=False)

# CorpApps Tower connection
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws3206\D$\Applications\CorpAppsTower\Resource_loading_CorpApp.mdb;')
sql_query = pd.read_sql_query('select User_Name from Resource', conn)
df = pd.DataFrame(sql_query)
df['Tower'] = 'CorpApps'
with open(r'C:\Billing_RL\template\export_data.csv', 'a', newline='') as fd:
    df.to_csv(fd, index=False, header=False)

# Analytics Tower connection
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws3206\D$\Applications\AnalyticsTower\Resource_loading_Analytics.mdb;')
# cursor = conn.cursor()
sql_query = pd.read_sql_query('select User_Name from Resource', conn)
df = pd.DataFrame(sql_query)
df['Tower'] = 'Analytics'
with open(r'C:\Billing_RL\template\export_data.csv', 'a', newline='') as fd:
    df.to_csv(fd, index=False, header=False)

# Labs Tower connection
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws3206\D$\Applications\LabsTower\Resource_loading_Labs.mdb;')
# cursor = conn.cursor()
sql_query = pd.read_sql_query('select User_Name from Resource', conn)
df = pd.DataFrame(sql_query)
df['Tower'] = 'Labs'
with open(r'C:\Billing_RL\template\export_data.csv', 'a', newline='') as fd:
    df.to_csv(fd, index=False, header=False)

# Web & Misc. Tower connection
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws3206\D$\Applications\WNMTower\Resource_loading_WebMisc.mdb;')
# cursor = conn.cursor()
sql_query = pd.read_sql_query('select User_Name from Resource', conn)
df = pd.DataFrame(sql_query)
df['Tower'] = 'Web & Misc'
with open(r'C:\Billing_RL\template\export_data.csv', 'a', newline='') as fd:
    df.to_csv(fd, index=False, header=False)

# Sales & Marketing Tower connection
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws3206\D$\Applications\SMTower\Resource_loading2.mdb;PWD=123456')
# cursor = conn.cursor()
sql_query = pd.read_sql_query('select User_Name from Resource', conn)
df = pd.DataFrame(sql_query)
df['Tower'] = 'Sales & Marketing'
with open(r'C:\Billing_RL\template\export_data.csv', 'a', newline='') as fd:
    df.to_csv(fd, index=False, header=False)
