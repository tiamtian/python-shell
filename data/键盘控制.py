from pynput.keyboard import Key, Controller

keyboard = Controller()
# 按下空格和释放空格
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)
# 按下a键和释放a键
# Type a lower case A ;this will work even if no key on the physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')

# Type two upper case As
keyboard.press('s')
keyboard.release('S')
# or 
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

# type 'hello world ' using the shortcut type method
keyboard.type('hello world')