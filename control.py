# (position form left to right,top to bottom)
# it is from top left of the screen you can top-left to be (0,0)
#for listening to mouse
#contolling your mouse
#listening to keystrokes
#controlling your keyboard

from pynput.mouse import Controller
from pynput.keyboard import Controller


def controlMouse():
    mouse=Controller()
    mouse.position=(100,200)

def controlKeyboard():
    keyboard=Controller()
    keyboard.type(" I can do anything")






