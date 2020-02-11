from insertionsort import *
import pygame

pygame.init()

def visualize(arr):
    return 3

toSort = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]

ret = sort(toSort)
visualize(ret)

