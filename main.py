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

