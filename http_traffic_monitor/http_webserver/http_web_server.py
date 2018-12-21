#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer


"""
class TestHTTPTrafficMonitor. Instantiates web server on port 8080 for displaying
      a. Current 10 second statistics of the HTTP traffic.
      b. Historic statistics of alarms and events.
 This class will handles any incoming request from the browser.
"""


class RequestCallBackHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(b"<html><head><title>Output Summary.</title></head>")
        self.wfile.write(b"<body><p> Historic Stats.</p>")
        self.wfile.write(b"<body><p>^^^^^^^^^^^^^^^^^^^.</p>")
        try:
            with open(HTTPWebServerDumpStats.history_file_path) as f:
                for line in f:
                    self.wfile.write(b"<p>%s</p>" % line.encode('utf8'))
                self.wfile.write(b"<body><p>--------------------.</p>")
        except:
            # print("Skipping Historic stats as the output is not generated yet.")
            self.wfile.write(b"<body><p>--------NONE--------.</p>")

        self.wfile.write(b"<body><p> Current Running Stats.</p>")
        self.wfile.write(b"<body><p>^^^^^^^^^^^^^^^^^^^^^^.</p>")
        try:
            with open(HTTPWebServerDumpStats.current_stats_file_name) as f:
                for line in f:
                    self.wfile.write(b"<p>%s</p>" % line.encode('utf8'))
                self.wfile.write(b"<body><p>--------------------.</p>")
        except:
            # print("Skipping current stats as the output is not generated yet.")
            self.wfile.write(b"</body><p>--------NONE--------.</p></html>")
        return


# This class will handles any incoming request from
# the browser
class HTTPWebServerDumpStats:
    current_stats_file_name = None
    history_file_path = None
    port = 8080

    def __init__(self,
                 current_stats_file_name,
                 history_file_path,
                 port):
        self.server = None
        HTTPWebServerDumpStats.current_stats_file_name = current_stats_file_name
        HTTPWebServerDumpStats.history_file_path = history_file_path
        HTTPWebServerDumpStats.port = port
        self.create_web_server()

    def create_web_server(self):
        try:
            # Create a web server and define the handler to manage the
            # incoming request
            self.server = HTTPServer(('', HTTPWebServerDumpStats.port),
                                     RequestCallBackHandler)
            print('Started httpserver on port ',
                  HTTPWebServerDumpStats.port)

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