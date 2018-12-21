#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080


# This class will handles any incoming request from
# the browser
class RequestCallBackHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(b"<html><head><title>Output Summary.</title></head>")
        self.wfile.write(b"<body><p> Historic Stats.</p>")
        self.wfile.write(b"<body><p>*******************.</p>")
        with open("../historic_stats.txt") as f:
            for line in f:
                self.wfile.write(b"<p>%s</p>" % line.encode('utf8'))
            self.wfile.write(b"<body><p>*******************.</p>")
        self.wfile.write(b"<body><p> Current Running Stats.</p>")
        self.wfile.write(b"<body><p>*******************.</p>")
        with open("../current_stats.txt") as f:
            for line in f:
                self.wfile.write(b"<p>%s</p>" % line.encode('utf8'))
            self.wfile.write(b"<body><p>*******************.</p>")
        self.wfile.write(b"</body></html>")
        return


# This class will handles any incoming request from
# the browser
class HTTPWebServerDumpStats:
    def __init__(self):
        self.server = None
        self.create_web_server()

    def create_web_server(self):
        try:
            # Create a web server and define the handler to manage the
            # incoming request
            self.server = HTTPServer(('', PORT_NUMBER), RequestCallBackHandler)
            print('Started httpserver on port ', PORT_NUMBER)

        except KeyboardInterrupt:
            print('^C received, shutting down the web server')
            self.server.socket.close()

    def listen_for_connections(self):
        try:
            # Wait forever for incoming http requests
            self.server.serve_forever()

        except KeyboardInterrupt:
            print('^C received, shutting down the web server')
            self.server.socket.close()


if __name__ == "__main__":
    server = HTTPWebServerDumpStats()
    server.listen_for_connections()