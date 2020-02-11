import pygame
from main import *
import time

pygame.init()
MAX = 300
screen = pygame.display.set_mode((MAX,MAX))
blue = (0, 0, 255)

def visualize(arr):
    x = 0
    y = 0
    for a in arr:
        pygame.draw.rect(screen, blue, (x,y,10,a*10))
        x += 15
    return 3

def sort(s):
    for i in range(len(s)):
        curr = s[i]
        j = i-1
        while(j>=0 and s[j]>curr):
            s[j+1] = s[j]
            j -= 1
            print(s)
        s[j+1] = curr
        screen.fill((0, 0, 0))
        visualize(s)
        pygame.display.update()
        time.sleep(1)
    return s