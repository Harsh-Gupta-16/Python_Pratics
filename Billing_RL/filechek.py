import os
import datetime

# if os.path.exists('Tracker_Data*'):
#     print('True') 
# else:
#     print('False')

incomplete_file = 'None'
wait = True
print(os.environ.get('userprofile') + '\OneDrive - Quest Diagnostics\\')
while wait == True:
    for filename in os.listdir(os.environ.get('userprofile') + '\\OneDrive - Quest Diagnostics\\Downloads'):
        if filename.endswith('crdownload'):
            incomplete_file = filename
            print(filename)
            wait = True
    if os.path.exists(os.environ.get('userprofile') + '\\OneDrive - Quest Diagnostics\\Downloads\\' + incomplete_file):
        print('yes')
    else:
        wait = False
        print('no')
        print(incomplete_file)

# fileendswith = "crdownloads"
# while fileendswith == "crdownloads":
#    for filename in os.listdir('.'):
#        if filename.endswith("crdownload"):
#            print(filename)
#        else:
#            fileendswith = "none"

# wait = True
# while(wait==True):
#     if os.path.exists('Tracker*'):
#         print('yes')
#     else:
#         wait=False
# userprofile = os.environ.get("userprofile").replace("/","//")
# print(os.path.exists('Order_and_Referring.csv.crdownload'))
# print(userprofile)
# for fname in os.listdir('.'):
#         if ('Tracker') in fname:
#             print('downloading files ...')
#             # time.sleep(15)
#         else:
#             # wait=False
#             print('false')

dateTimeObj = datetime.datetime.now()
timestamp = dateTimeObj.strftime("%d%m%Y_%H%M%S")
print(timestamp)
