import os
import time

hours,minutes,seconds = 0,0,0
while(True):
  print(hours,":",minutes,":",seconds)
  seconds+=1
  if(seconds==60):
    seconds=0
    minutes+=1
  if(minutes==60):
    minutes=0
    hours+=1
  time.sleep(1)

os.system('cls')
