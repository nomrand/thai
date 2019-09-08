cd "$(dirname "$0")"
#IP=`ipconfig getifaddr en0`
IP=`ifconfig | grep "inet 172.21" | awk '{print $2}'`
# 4443=>https, other=>http
PORT=4443

python __httpsev_tmp/python_script/replace.py __httpsev_tmp/qrcode.org.html __httpsev_tmp/qrcode.html ${IP} ${PORT}
open __httpsev_tmp/qrcode.html

python __httpsev_tmp/python_script/simple-https-server.py ${IP} ${PORT}
