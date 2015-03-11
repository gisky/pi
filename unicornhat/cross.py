import unicornhat as uh
import time
from random import randint

points = []
 
class LightPoint():

  def __init__(self):
    self.direction = randint(1,4)
    if self.direction == 1:
      self.x = randint(0,7)
      self.y = 0
    elif self.direction == 2:
      self.x = 0
      self.y = randint(0,7)
    elif self.direction == 3:
      self.x = randint(0,7)
      self.y = 7
    else:
      self.x = 7
      self.y = randint(0,7)
    self.colour = []
    for i in range(0,3):
      self.colour.append(randint(100,255))
    
def updatePositions():
  for point in points:
    if point.direction == 1:
      point.y += 1
      if point.y > 7:
        points.remove(point)
    elif point.direction == 2:
      point.x += 1
      if point.x > 7:
        points.remove(point)
    elif point.direction == 3:
      point.y -= 1
      if point.y < 0:
       points.remove(point)
    else:
      point.x -= 1
      if point.x < 0:
        points.remove(point)

def plotPoints():
  uh.clear()
  for point in points:
    uh.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2]) 
  uh.show()
  
while (True):
  for j in range (1,3):
    if (len(points) < 30 and randint(0,5) > 1):
      points.append(LightPoint())
  plotPoints()
  updatePositions()
  time.sleep(0.03)

    
