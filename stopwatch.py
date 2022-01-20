import os
import time

hours,minutes,seconds = 0,0,0
while(True):
  print(hours,":",minutes,":",seconds)
  time.sleep(1)
  seconds+=1
  if(seconds==60):
    seconds=0
    minutes+=1
  if(minutes==60):
    minutes=0
    hours+=1
  os.system('cls')
