from http.server import BaseHTTPRequestHandler
import socketserver
import signal
import sys
import os
import platform


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print("Writing \"Hello from '" + str(platform.node()) + "'!\"")
            self.wfile.write(bytes("Hello from '" + str(platform.node()) + "'!\n", "utf-8"))
        else:
            self.send_response(400)


class Server(object):
    def __init__(self, srv_port=8080):
        self.srv_port = srv_port

        if os.name != 'nt':
            socketserver.ThreadingTCPServer.allow_reuse_address = True

        self.server = socketserver.ThreadingTCPServer(("", srv_port), MyHandler)

        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signal, frame):
        print('\nServer exit!')
        self.Stop()
        sys.exit(0)

    # Start server (needed for threading, which is needed for testing)
    def Start(self):
        print("Starting pyechoserver on port " + str(self.srv_port) + "...")
        self.server.serve_forever()

    # Stop server
    def Stop(self):
        print("Stopping pyechoserver...")
        self.server.server_close()
        print("...stopped.")
