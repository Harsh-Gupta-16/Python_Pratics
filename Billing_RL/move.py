import os

# user = os.environ.get('userprofile')
# cmd = 'move ' + user + '\\downloads\\*xls C:\Billing_RL\inprocess'
# # os.renames(user+'\\downlaod\\*xls','C:\\Billing_RL\\inprocess')
# os.system(cmd)


user = os.environ.get('userprofile')
# Checking and Moving the file from download location to specific location
cmd = 'if exist ' + user + '\\downloads\\*.xls ( move ' + user + '\\downloads\\*xls C:\\Billing_RL\\inprogress )'
print(cmd)
os.system(cmd)

user = os.environ.get('userprofile') + '\\' + '"OneDrive - Quest Diagnostics"'
cmd = 'if exist ' + user + '\\downloads\\*.xls ( move ' + user + '\\downloads\\*xls C:\\Billing_RL\\inprogress)'
os.system(cmd)
print(cmd)