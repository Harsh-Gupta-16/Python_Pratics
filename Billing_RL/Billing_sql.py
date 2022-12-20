import pyodbc
import pandas as pd

conn = pyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Harsh.x.Gupta\Desktop\TPInfo.mdb;")
# conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\qdcws0486\ECEDIGS\ECEDIGS\scripts\Comm\Profiles\Profiles.mdb;")
cursor = conn.cursor()
# cursor.execute('select * from DEV_OUTBOUND')
# cursor.execute('select TP_Id from Trading_Partner')
# f = open("userlist.txt", "w")
# row: object
# for row in cursor.fetchall():
#     f.write(str(row))
# f.close()
sql_query = pd.read_sql_query(''' 
                              select TP_Id from Trading_Partner
                              '''
                              , conn)
df = pd.DataFrame(sql_query)
df.to_csv('user.csv', index=False)
# for row in cursor.fetchall():
#     print(str(row))
sql_query = pd.read_sql_query(''' 
                              select TP_Name from Trading_Partner
                              '''
                              , conn)
df = pd.DataFrame(sql_query)
df.to_csv('user.csv', mode='a', index=False, header = False)
