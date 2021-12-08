from socket import *
import threading
from func_timeout import func_set_timeout

sem = threading.Semaphore(5)
threadLock = threading.Lock()

@func_set_timeout(3)
def connScan(Host, Port):
    try:
        print("scan over1")
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((Host, Port))
        threadLock.acquire()
        print(Host,Port,"is open")
    except:
        print("scan over2")
        threadLock.acquire()
        pass
    finally:
        print("scan over")
        threadLock.release()
        conn.close()

def portScan(Host, ports):
    try:
        connScan(Host, ports)
    except:
        pass

# 192.168.31.110-111
# 445,555,666 或者 445
def fullHostsinglePort():
    ip = input("Scan ip:")
    ports = input("ports:")
    newip = ip.rsplit(".",1)
    forwardIp = newip[0]
    afterIp = newip[1]
    newip = afterIp.split('-')
    newPort = ports.split(',')

    for i in range(int(newip[0]),int(newip[1])+1):
        newip = forwardIp + "." + str(i)
        for port in newPort:
            p = int(port)
            th = threading.Thread(target=portScan, args=(newip, p))
            th.start()

# 192.168.31.111
# 192.168.31.0/24
def fullHostPort():
    ip = input("Scan ip:")
    newip = ip.rsplit('.', 1)
    if newip[1] == "0/24":
        for host in range(0,256):
            newip = str(newip[0]) + "." + str(host)
            for port in range(1,65536):
                th = threading.Thread(target=portScan, args=(newip, port))
                th.start()
    elif newip[1] <= "256":
        for port in range(1, 65536):
            th = threading.Thread(target=portScan, args=(ip, port))
            th.start()
    else:
        print("input mistake!")

def main():
    mode = input("select scan mode:")
    if mode == '1':
        fullHostsinglePort()
    elif mode == '2':
        fullHostPort()
    else:
        print("select mistake")

if __name__ == '__main__':
    main()

