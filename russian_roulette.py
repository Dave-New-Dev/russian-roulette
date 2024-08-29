from random import randint as rdmNo
import subprocess
import ctypes
import sys
from time import sleep

def shot():
  ctypes.windll.shell32.ShellExcecuteW(
    None, "runas", "powershell", '-Command "wininit"', None, 1
  )

def run(cmd):
    subprocess.run(cmd, shell=True, capture_output=False)

acceptWords = [
  'yes','ye','sure','ofc','of course','definitely','absolutely','with pleasure','i do','i trust my fortune','i dare','indeed','positive','true'
]
denyWords = [
  'no','nah','no thanks','ofc not','of course not','definitely not','absolutely not',"i don't",'i do not','i do not trust my fortune',"i'm scared","i am scared","i'm afraid",'i am afraid',"i'm too scared",'i am too scared','negative','false'
]
def choice(choice):
  global acceptWords
  global denyWords
  acptWords = acceptWords
  dnyWords = denyWords

  choice = choice.lower()
  if choice in acptWords:
    return True
  elif choice in dnyWords:
    return False
  else:
    return "Punish"

if __name__ == '__main__':
    print("A gun. Six slots; 1 round. Good luck, but you probably won't need it.\n")
    sleep(1.25)
    print("Spinning barrel.")
    sleep(0.7)
    print("Spinning barrel..")
    sleep(0.7)
    print("Spinning barrel...")
    loadedSlot = rdmNo(1,6)
    shootingSlot = rdmNo(1,6)
    sleep(1)
    print("Now...\n")
    sleep(1)
    choice = input("Do you trust your fortune to pull the trigger or are you too scared?")
    if choice(choice):
      if shootingSlot == loadedSlot:
        print("Ah... what a shame...\n")
        sleep(0.4)
        print("Well better luck next time- ",end=" ")
        sleep(0.3)
        print("Oh wait there won't be a next time-",end=" ")
        sleep(0.2)
        print("Oh wait nevermind! This isn't even real!")
        sleep(1)
        shot()
      else:
        sleep(0.4)
        print("As expected!\n")
        sleep(0.3)
        print("I commend you for your fortune.",end=" ")
        sleep(0.2)
        print("Well done.")
    elif choice(choice) == False:
      print("Well that's a shame...")
      sleep(0.3)
      print("I won't be seeing you off then...")
      run("shutdown -s -t 3")
    elif choice(choice) == "Punish":
      print("Had I known you'd be this rude, I would've kicked you out already.")
      sleep(0.07)
      print("You need to be taught a lesson...")
      sleep(0.4)
      run("shutdown /p")
    else:
      raise Exception("how did this happen...") #This may or may not happen
