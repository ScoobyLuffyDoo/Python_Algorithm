import random
import time

array = []
sortedArray = []

# generate a radnom array
for ammount in range(10):
    array.append(random.randint(1,10))
print(array)

timer_Start = time.perf_counter()
for i in range((len(array))-1):
    for j in range(0,(len(array)) -i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1],array[j]
timer_Stop = time.perf_counter()    
print(timer_Stop -timer_Start /60)       
print('final')            
print(array)