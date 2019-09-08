# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys
import os

httpd = HTTPServer((sys.argv[1], int(sys.argv[2])), SimpleHTTPRequestHandler)
if sys.argv[2] == "4443":
    httpd.socket = ssl.wrap_socket(
        httpd.socket, certfile='__httpsev_tmp/server.pem', server_side=True)
print("WEB SERVER https://"+sys.argv[1]+":"+sys.argv[2]+" START!")
httpd.serve_forever()
