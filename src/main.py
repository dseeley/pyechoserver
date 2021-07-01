import pyechoserver
import argparse


def main(srv_port):
    oTestServer = pyechoserver.Server(srv_port)
    oTestServer.Start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='Server port', default='8080')
    args = parser.parse_args()

    main(int(args.port))
