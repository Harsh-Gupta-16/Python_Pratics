import datetime

# creating time stamp
dateTimeObj = datetime.datetime
timestamp = dateTimeObj.now().strftime("%d%m%Y_%H%M%S")

# Set date for automatic
fromdate = dateTimeObj.now().strftime("%m/01/%Y")
print(fromdate)
todate = (dateTimeObj.now()-datetime.timedelta(days=1)).strftime("%m/%d/%Y")
print(todate)