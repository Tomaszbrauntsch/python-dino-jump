#http://www.trex-game.skipser.com/ <-- This is the website for the game
import PIL.ImageGrab as ImageGrab
import pyautogui
import time
import sys
pyautogui.FAILSAFE = True

box_area = (334, 400, 364, 438)# Area of box top left and bottom left cords
Big_Plant = (16.5, 3.5) #Top / Big plants
Small_Plant = (21.5, 33.5) # Middle
Plantthree = (15.5, 36.5) #Bottom

class coords():
    replaybtn = (481, 399) #<- Coordinate of replay button
    dino = (274, 405) #Coordinate of dinosaur

def replaygame():
    pyautogui.click(coords.replaybtn)

def jump():
    pyautogui.keyDown('Space')
    time.sleep(0.05)

replaygame()
while True:
    try:
        box = ImageGrab.grab(box_area)
        BP = box.getpixel(Big_Plant)
        PT = box.getpixel(Plantthree)
        SP = box.getpixel(Small_Plant)
        if BP == (83, 83, 83) or SP == (83, 83, 83):
            jump()
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit(0)
