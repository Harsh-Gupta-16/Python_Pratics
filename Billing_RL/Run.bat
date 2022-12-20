@ echo off
cd /d C:\Billing_RL\inprogress
Echo ===================^>Start Running the Program ^<==========================

py C:\Billing_RL\Biiling_RL.py

Echo ===================^>Program Completed ^<==============================
Echo.
Echo ===================^>Archiving the File ^<==============================
move Billing_Resource_loading_*xls C:\Billing_RL\Archive
pause