cd /d %~dp0
set IP=192.168.21.48
REM 4443=>https, other=>http
set PORT=4443

set PYTHON=D:\mydocument\program\anaconda\python.exe

%PYTHON% __httpsev_tmp\python_script\replace.py __httpsev_tmp\qrcode.org.html __httpsev_tmp\qrcode.html %IP% %PORT%
start __httpsev_tmp\qrcode.html

%PYTHON% __httpsev_tmp\python_script\simple-https-server.py %IP% %PORT%
