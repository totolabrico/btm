
"""
def on_press(key):
    myKey=getMap(key)
    analyseCom(idMenu,myKey,partition)

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released

def listenKeys():
    with keyboard.Listener(
	on_press=on_press,
	on_release=on_release) as listener:
	    listener.join()
"""
