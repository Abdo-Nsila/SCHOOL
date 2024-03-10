import random
import time
import pyautogui as pya

while True:
    X = random.randint(600,1000)
    Y = random.randint(200,1000)
    pya.moveTo(X,Y,1)
    time.sleep(2)