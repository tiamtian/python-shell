from socket import *

def image_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('0.0.0.0', 5555))
    s.listen(5)
    sock, addr = s.accept()
    print('connnect from ', addr)
    photo = s.recv(1024)
    photo = b'new_' + photo
    f = open(photo, 'wb')
    while True:
        data = sock.recv(1024)
        if not data:
            break
        f.write(data)
    f.close()