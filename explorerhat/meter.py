import explorerhat
import time

while True:
  level  = explorerhat.analog.one.read()
  for i in range(0,4):
   if (level > float(i+1)):
     explorerhat.light[i].on()
   else:
    explorerhat.light[i].off()
  time.sleep(0.25)
