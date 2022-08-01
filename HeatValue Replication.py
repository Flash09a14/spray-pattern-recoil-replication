# screen usage module
import pygame

# random generation module
from random import randint

#time module
import time


pygame.init()

running = True
fire_rate = 0.3

# main
while running:
    heatValuesX1 = 960 # resolution divided by 2 (width) this makes sure it's in the middle (usually where the crosshair is)
    heatValuesY1 = 520 # resolution divided by 2 (height) this makes sure it's in the middle (usually where the crosshair is)
    # arrays (lists) of heat values (per shot)
    heatValuesX2 = [970, 950, 940, 980]
    heatValuesY2 = [450, 440, 430, 435]
    heatValuesX3 = [975, 955, 950, 970]
    heatValuesY3 = [370, 390, 350, 340]
    # random number genrator (for random recoil patterns)
    number1Y = heatValuesY1
    number1X = heatValuesX1
    number2X = heatValuesX2[randint(0,3)]
    number2Y = heatValuesY2[randint(0,3)]
    number3X = heatValuesX3[randint(0,3)]
    number3Y = heatValuesY3[randint(0,3)]
    # screen display
    scrn = pygame.display.set_mode((1920, 1040))
    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # prints heat value and draws bullet (square on random assigned position/coordinate on the x and y values)
    print("heat value is 1")
    pygame.draw.rect(scrn, (255, 0, 0), pygame.Rect(number1X, number1Y, 30, 30), border_radius=10)
    time.sleep(fire_rate)
    print("heat value is 2")
    pygame.draw.rect(scrn, (0, 255, 0), pygame.Rect(number2X, number2Y, 30, 30), border_radius=10)
    time.sleep(fire_rate)
    print("heat value is 3")
    pygame.draw.rect(scrn, (0, 0, 255), pygame.Rect(number3X, number3Y, 30, 30), border_radius=10)
    # delay (reload)
    time.sleep(0.7)
    print("reloading")

    # display flip
    pygame.display.flip()

    # green is where it lands on the second shot

    # blue is on the third shot (highest heat value)

    # red stays constant as it is on the first shot (1st heat value)

    # more explanation on garbaj's video on this topic https://www.youtube.com/watch?v=XNkijakpf9Y

    # he's pretty great at explaining stuff in development, check him out