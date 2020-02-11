import pygame
from main import *
import time
screen = None
def init(arr):
    global screen
    global pad
    global MAX
    pad = 15
    MAX = len(arr) * (10+pad)
    screen = pygame.display.set_mode((MAX,MAX))

def visualize(arr):
    
    blue = (0, 0, 255)
    x = 0
    y = 0
    for a in arr:
        pygame.draw.rect(screen, blue, (x,y,10,a*10))
        x += pad
    return 3

def sort(s):
    pygame.init()
    times = 0
    for i in range(len(s)):
        curr = s[i]
        j = i-1
        while(j>=0 and s[j]>curr):
            s[j+1] = s[j]
            j -= 1
            print(s)
            times += 1
        s[j+1] = curr
        screen.fill((0, 0, 0))
        visualize(s)
        pygame.display.update()
        times += 1
        time.sleep(1)
    print("Times gone through: ", times)
    print(len(s))
    return s