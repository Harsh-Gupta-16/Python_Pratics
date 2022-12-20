@echo off
REM for /F "usebackq tokens=1,2,3,4 delims=\" %%a in ("L:\Harsh_Temp\AutomateXmit\ECEDIGSXmitList.txt") do REM echo %%d

for /F "usebackq tokens=1,2,3,4 delims=\" %%a in ("L:\Daily_Folder_Monitoring\Temp_Files\InSearchFolder\ECEDIGSXmitList.txt") do (
echo TP.%%d.837.OUTBOUND
copy null > T:\ecedigs\PF_PostOffice\STANDARD\PROD\TP.%%d.837.OUTBOUND
)
pause