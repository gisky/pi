import unicornhat as uh
import time
from random import randint

uh.rotation(0)
uh.brightness(0.2)
heights = []

def setup():
  global heights
  heights =[]
  for i in range (0,6):
   heights.append(0)
  uh.off()
  for i in range (0,8):
    uh.set_pixel(0,i,255,255,255)
  for i in range (0,8):
    uh.set_pixel(7,i,255,255,255)
  for i in range (1,7):
    uh.set_pixel(i,0,255,255,255)
  uh.show()

def dropBall():
  ballColour = [randint(100,255),randint(100,255),randint(100,255)]
  ballColumn = randint(0,5)
  while (heights[ballColumn] == 7):
    ballColumn = randint(0,5)
  height = heights[ballColumn]
  ballY = 7
  uh.set_pixel(ballColumn + 1, ballY , ballColour[0], ballColour[1], ballColour[2]) 
  uh.show()
  dropcount = 6-height
  for y in range (0,dropcount):
    uh.set_pixel(ballColumn+1, ballY, 0,0,0)
    ballY -= 1
    uh.set_pixel(ballColumn+1, ballY, ballColour[0], ballColour[1], ballColour[2])
    uh.show()
    time.sleep(0.02)
  heights[ballColumn] += 1
     
setup()

while True:
 for i in range (0,42):
   dropBall()
 time.sleep(1) 
 setup()

    
