from pynput.keyboard import Key, Controller
import time
import sys

keyboard = Controller()

toDo = sys.argv[1]
howLong = float(sys.argv[2])
print "Going " + toDo + " for " + str(howLong) + " seconds"

def switchTabs():
	keyboard.press(Key.alt)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.release(Key.alt)

	time.sleep(0.5)

def goForward(goTime):

	switchTabs()
	keyboard.press(Key.right)
	time.sleep(goTime)
	keyboard.release(Key.right)

	switchTabs()

def goBackward(goTime):
	switchTabs()

	keyboard.press(Key.left)
	time.sleep(goTime)
	keyboard.release(Key.left)
	
	switchTabs()

if toDo == 'forw':
	goForward(howLong)
elif toDo == 'back':
	goBackward(howLong)

#print(type(time))


