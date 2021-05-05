import random
import time

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
# if they are in wrong order.

array = []
sortedArray = []

# generate a radnom array
for ammount in range(5000):
    array.append(random.randint(1,5000))

timer_Start = time.perf_counter()

# Bubble Sorting 
for i in range((len(array))-1):
    for j in range(0,(len(array)) -i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1],array[j]

timer_Stop = time.perf_counter()    
print(timer_Stop -timer_Start /60)       
print('final')            
