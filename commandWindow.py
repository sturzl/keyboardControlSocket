#import socket
import sys, pygame
import time

#constants
windowSize = width, height = 800, 600
#displayed in the window t ogive directiosn to the driver
instructionTextLines =  ('window must be active ("on top") for commands to work','space bar is stop')
activeColor = (0,175,0)
inactiveColor = (255,0,0)
textColor = (0,0,0)
screen = pygame.display.set_mode(windowSize)

################window initialization#################################

#makes hte window, sets color, displays text etc.
def initializeWindow():
	pygame.init()
	setBackgorundColor(activeColor)
	pygame.display.set_caption('CWRU NASA RMC 2015-2016')
	displayIntructionText()

def displayIntructionText():
	for lineNumber,lineText in enumerate(instructionTextLines):
		displayText(lineText, lineNumber)

#creating the text object, putting it in the window, updating
#takes in a string
def displayText(text, lineNumber):
	font = pygame.font.SysFont("monospace", 20)
	textSurface, textContainer = getTextObject(text, font)
	textContainer.center = (width/2,10+25*lineNumber)
	screen.blit(textSurface, textContainer)
	pygame.display.update()

#getting the font, text rectangle etc.
#takes in the string of fonts and a pygame Font
def getTextObject(text, font):
	textSurface = font.render(text, True, textColor)
	return textSurface, textSurface.get_rect()

def setBackgorundColor(colorTuple):
	screen.fill(colorTuple)
	pygame.display.update()


#########################Setting up the socket ###########################




#################################  Gettting Keyboard state ################################

#gets the currently pressed keys and sends them over the socket
def sendKeyboard():
	currentlyPressedKeys = getNextKeys()
	sendKeys(currentlyPressedKeys);

#Waits for a keyboard event, determines which keys are pressed after each keyboard event,
#returns the list of currently pressed keys
def getNextKeys():
	return getCurrentKeys()

def sendKeys(keys):
	socket.send(keys)

def getCurrentKeys():
	pygameEvent = pygame.event.wait()
	if pygameEvent.event.event_name() == "KEYDOWN":
		return pygame.key.getPressed();


############### Main program ####################################

initializeWindow()
#initializeSocket()
while(True):
#	sendKeyboard()
	print pygame.event.wait()

