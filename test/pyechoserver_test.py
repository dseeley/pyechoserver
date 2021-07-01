import threading
import unittest
import os

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import src.pyechoserver as pyechoserver


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        self.srv_port = int(os.environ["SRV_PORT"]) if "SRV_PORT" in os.environ else 8090
        self.oTestServer = pyechoserver.Server(self.srv_port)
        self.httpd_srv_thread = threading.Thread(target=self.oTestServer.Start)
        self.httpd_srv_thread.setDaemon(True)
        self.httpd_srv_thread.start()

    def tearDown(self):
        """Called after every test case."""
        self.oTestServer.server.shutdown()
        self.oTestServer.Stop()

    def test1(self):
        """test1"""
        response = urlopen('http://localhost:' + str(self.srv_port))
        resp_data = response.read()
        self.assertEqual(response.code, 200)
        self.assertRegex(resp_data, bytes("Hello from '.*?'!\n", "utf-8"))
