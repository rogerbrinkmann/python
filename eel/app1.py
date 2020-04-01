import eel

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(data):
    print(data)

say_hello_py('1')
eel.say_hello_js('2')   # Call a Javascript function

eel.start('main1.html',mode="chrome", size=(500, 500))    # Start