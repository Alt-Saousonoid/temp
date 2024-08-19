@echo off

:: Run the scripts in parallel
start "" cmd /c "python server.py test.csv 30 & pause"
start "" cmd /c "python client.py client1.csv prevalentHyp  & pause"
start "" cmd /c "python client.py client2.csv TenYearCHD  & pause"

:: Wait for all processes to finish
echo All scripts are running in parallel.
