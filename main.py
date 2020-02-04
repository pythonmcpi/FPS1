# Format Code Later: black.now.sh

from GameEngine import Screen
import time
import random
import math
import sys
import os

screenSize = (850,800)
screen = Screen(screenSize, (100,100), "FPS1")

""" Copied from snake.py
# Screen can do
# screen.fillbg((R,G,B))
# screen.drawrect((X1,Y1),(X2,Y2),(R,G,B))
# screen.drawline((X1,Y1),(X2,Y2),(R,G,B))
# screen.write(TEXT,(X,Y),(R,G,B),(FONTNAME,FONTSIZE,BOLD,ITALIC,UNDERLINE))
# screen.bindkey(KEY,FUNCTION)
## screen.unbindkey(BINDID) BINDID is returned by the bind function.

# Eventloop Processing Snake Draw Code and Win Detection Design:
# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
""" # Just for note

# Also screen.mainloop() calls tkinter's mainloop()
# And screen.after(function,timeout,*args) calls tkinter's after()
# I also added a screen.drawcircle()

tickSpeed = 50

def getNewRelativePos(speed, angle):
    return [speed*math.cos(angle),speed*math.sin(angle)]

def getBounds():
    return screenSize[:]

class Object:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

class Moveable(Object): # Name comes from the 'Moveable' class from Tanks.jar
    def __init__(self, pos, angle, speed):
        super().__init__(pos)
        self.angle = angle
        self.speed = speed

    def tick(self):
        xOffset, yOffset = getNewRelativePos(self.speed, self.angle)
        self.x, self.y += xOffset, yOffset

class Bullet(Moveable):
    def __init(self, pos, angle, speed):
        super().__init__(pos)

    def tick(self):
        super().tick()
        if not self.checkBounds():
            self.bounce()

    def checkBounds(self): # Need to update this functions when I implement Obstacles
        boundX, boundY = getBounds()
        if not 0 =< self.x =< boundX: # If speed is too fast, it will be glitchy, bullets will not bounce properly. Tickspeed must be pretty high so I can keep speed low, but if tickspeed is too fast the game will lag severely.
            return False
        elif not 0 =< self.y =< boundY:
            return False
        else:
            return True

    def bounce(self):
        pass
