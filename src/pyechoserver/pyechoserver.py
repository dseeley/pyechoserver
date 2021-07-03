from http.server import BaseHTTPRequestHandler
import socketserver
import signal
import sys
import os
import platform
import socket


# Returns the "primary" IP on the local machine (the one with a default route).
# From https://stackoverflow.com/a/28950776/12491741
def get_default_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))  # doesn't have to be reachable
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return_string = "Hello from '" + str(platform.node()) + "' (" + get_default_ip() + ")!"
            print("Writing \"" + return_string + "\"\n")
            self.wfile.write(bytes(return_string + "\n", "utf-8"))
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
