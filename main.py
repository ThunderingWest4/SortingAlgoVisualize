from insertionsort import *

toSort = [6, 12, 4, 7, 7, 1, 3, 7, 19, 2, 4, 3, 3, 2, 15, 14, 16, 17, 8, 9, 1, 0]
init(toSort)
ret = sort(toSort)
import time
for i in range(50):
    visualize(ret)
    pygame.display.update()
    time.sleep(0.5)



