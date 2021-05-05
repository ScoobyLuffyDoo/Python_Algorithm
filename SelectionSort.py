import random
import time

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

array = []
sortedArray = []

# generate a radnom array
for ammount in range(5000):
    array.append(random.randint(1,5000))
    
timer_Start = time.perf_counter()

# Selection Sorting
for  i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[i],array[j] = array[j],array[i]

timer_Stop = time.perf_counter()    
print(timer_Stop -timer_Start /60)
print("final")
#print(array)