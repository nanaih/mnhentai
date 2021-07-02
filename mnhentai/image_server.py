import os
import http.server
import socketserver
from socket import gethostname, gethostbyname 

# fill with the ABSOLUTE path to all your doujins
# this HAS to be the same path used in nhentai/initialize/
DOUJINS_PATH = ''
IMAGES_PORT = 6969  # change if you have other stuff running on this port


if __name__ == '__main__':
    try:
        os.chdir(DOUJINS_PATH)
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer((gethostbyname(gethostname()), IMAGES_PORT), Handler)
        print('Serving ' + DOUJINS_PATH + ' directory @ ' + gethostbyname(gethostname()) + ':' + str(IMAGES_PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        exit(0)
