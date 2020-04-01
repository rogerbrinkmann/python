import eel
import random

eel.init('web')

@eel.expose
def py_random():
    return random.random()


eel.start('main3.html', mode='chrome')