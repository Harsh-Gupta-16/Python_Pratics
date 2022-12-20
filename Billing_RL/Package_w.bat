@ echo off
REM Moving Python installing folder and set the path

Echo ===================^> Installing Pyhton ^<===============================
REM tar -xf Python39.zip -C C:\Billing_RL\
set pythn=C:\Billing_RL\Python39\python.exe
set pip=C:\Billing_RL\Python39\Scripts\pip.exe
Echo ===================^> Start Installing Package ^<==========================
echo - Installing Pandas Package
echo.
%pythn% %pip% install pandas

echo -  Installing XLWT Package
echo.
%pythn% %pip% install xlwt

echo -  Installing Selenium Package
echo.
%pythn% %pip% install selenium

echo -  Installing Beautiful Soup Package
echo.
%pythn% %pip% install bs4

echo -  Installing LXML Package
echo.
%pythn% %pip% install lxml

echo -  Installing Shutil Package
echo.
%pythn% %pip% install pytest-shutil

Echo ===================^> All Package Installed ^<==========================
Echo. 
Echo ===================^> Creating Directory ^<==========================
mkdir C:\Billing_RL\inprogress
mkdir C:\Billing_RL\Archive
mkdir C:\Billing_RL\drivers
Echo ===================^> Creating Directory Completed ^<==========================
Echo. 
Echo ===================^> Downlaod Web Driver ^<==========================
REM start https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip
REM TIMEOUT /T 30 /NOBREAK
if exist %userprofile%\Downloads\chromedriver_win32* ( tar -xf %userprofile%\Downloads\chromedriver_win32.zip -C C:\Billing_RL\drivers )
if exist %userprofile%\"OneDrive - Quest Diagnostics"\Downloads\chromedriver_win32* ( tar -xf %userprofile%\"OneDrive - Quest Diagnostics"\Downloads\chromedriver_win32.zip -C C:\Billing_RL\drivers )
Echo ===================^> Web Driver Downlaoded ^<==========================
Echo .
Echo ===================^> Creating RUN File ^<==========================
copy Biiling_RL.py C:\Billing_RL\
Echo @ echo off > C:\Billing_RL\Run.Bat
Echo cd /d C:\Billing_RL\inprogress >> C:\Billing_RL\Run.Bat
Echo Echo =================== Start Running the Program ========================== >> C:\Billing_RL\Run.Bat
Echo Echo. >> C:\Billing_RL\Run.Bat
Echo py C:\Billing_RL\Biiling_RL.py >> C:\Billing_RL\Run.Bat
Echo Echo. >> C:\Billing_RL\Run.Bat
Echo Echo =================== Program Completed ============================== >> C:\Billing_RL\Run.Bat
Echo pause >> C:\Billing_RL\Run.Bat
Echo =================== Setup Installation Complete ========================== 

Pause