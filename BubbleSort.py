import random
import time

array = []
sortedArray = []

# generate a radnom array
for ammount in range(100000):
    value =random.randint(1,1000000)
    array.append(value)
# print array

# Sort array
Sort_timerstart = time.perf_counter()
length = len(array)
for i in range(length -1): 
    # Sorting from Low to high
    for j in range(i +1,length):
        if array[i] > array[j]:
            tempdata = array[i]
            array[i] = array[j]
            array[j] = tempdata
    sortedArray = array
Sort_timerend = time.perf_counter()

print('Sorting Time : '+str(Sort_timerend - Sort_timerstart))