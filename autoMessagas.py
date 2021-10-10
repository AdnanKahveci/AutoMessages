from time import sleep
import pyautogui

from random import randint

noOfMessages = 20

def name():
    name_list=["name1","name2","name3","name4","name5"]

    rand_name= name_list[randint(0,len(name_list)-1)]
    return rand_name

while True:
    pyautogui.typewrite(f"admasin {name()}")
    sleep(.600)
    pyautogui.typewrite("\n")
    sleep(2)

    noOfMessages=noOfMessages - 1

    if noOfMessages ==0:
        break
