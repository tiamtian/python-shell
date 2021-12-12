from socket import *
localHost = "0.0.0.0"
remoteHost = "127.0.0.1"

localPort = 9988
remotePort = 8000

def procData(data):
    return data

print("Map Server start from " + localHost + ":" + str(localPort) + " to " + remoteHost + ":" + str(remotePort) + "\r\n")

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
server.bind((localHost,localPort))
server.listen(5)
print(localHost + " Server start at " + str(localPort) + "\r\n");

client = socket(AF_INET, SOCK_STREAM)
client.connect((remoteHost, remotePort))
print(localHost + " client connect to " + remoteHost + ":" + str(remotePort) + "\n")
ss, addr = server.accept()

while 1:
    print("connect from", addr)
    msg = ss.recv(2048)
    print("get: " + repr(msg) + "\r\n")
    client.send(msg)
    print("send:" + repr(msg) + "\r\n")
    buf = client.recv(2048)
    print("get: " + repr(buf) + "\r\n")
    ss.send(buf)
    print("send: " + repr(buf) + "\r\n")