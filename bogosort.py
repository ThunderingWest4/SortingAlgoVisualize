import random

def bogosort(arr):
  n = 1
  while(not checkSort(arr)):
    random.shuffle(arr)
    print(f"Trial {n}: {arr}")
    n += 1
  return arr
  
def checkSort(arr):
  for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]): return False
  return True
