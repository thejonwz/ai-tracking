# Sofwerx ai-tracking RC Car controller script
# To run this, in Terminal, run
# python switch_n_type.py <direction> <time>
# ex: python switch_n_type.py forw 0.5


# import dependencies
from pynput.keyboard import Key, Controller
import time
import sys

# create Controller object
keyboard = Controller()

# get arguments, [1] is either 'forw' or 'back'
# [2] decimal or int time to go in seconds
toDo = sys.argv[1]
howLong = float(sys.argv[2])
print "Going " + toDo + " for " + str(howLong) + " seconds"

# switches window focus to previously focused window
# make sure the BLDC tool was the last focus
def switchTabs():
	keyboard.press(Key.alt)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.release(Key.alt)

	time.sleep(0.5)

# switches focus, presses key, waits, unpresses key, switches back to terminal
# a time of 0.5 seconds makes the car travel ~5 feet
def goForward(goTime):

	switchTabs()
	keyboard.press(Key.right)
	time.sleep(goTime)
	keyboard.release(Key.right)

	switchTabs()

# switches focus, presses key, waits, unpresses key, switches back to terminal
# back time needs to be a bit longer than forward time
def goBackward(goTime):
	switchTabs()

	keyboard.press(Key.left)
	time.sleep(goTime)
	keyboard.release(Key.left)

	switchTabs()

# forward or backward
if toDo == 'forw':
	goForward(howLong)
elif toDo == 'back':
	goBackward(howLong)
