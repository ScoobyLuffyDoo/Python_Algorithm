from multiprocessing import Process
import random as rnd
import time
import string

processes = []
BubleArray =[]
array = []
SelectionArray =[]
bubbleTimer =0
SelectionTimer =0
mainTimer_Start =0

def doBubbleSort():
    global BubleArray
    global bubbleTimer
    bubbleInput =array
    timer_Start = time.perf_counter()
    for i in range((len(bubbleInput))-1):
        for j in range(0,(len(bubbleInput)) -i-1):
            if bubbleInput[j] > bubbleInput[j+1]:
                bubbleInput[j], bubbleInput[j+1] = bubbleInput[j+1],bubbleInput[j]    
    BubleArray = bubbleInput
    timer_Stop = time.perf_counter()    
    bubbleTimer =float(timer_Stop-timer_Start)
    

def doSelectionSort():
    global SelectionArray
    global SelectionTimer
    selectionInput = array
    timer_Start = time.perf_counter()
    for  i in range(len(selectionInput)):
        for j in range(i + 1, len(selectionInput)):
            if selectionInput[i] > selectionInput[j]:
                selectionInput[i],selectionInput[j] = selectionInput[j],selectionInput[i]
    SelectionArray = selectionInput    
    timer_Stop = time.perf_counter() 
    SelectionTimer =float(timer_Stop-timer_Start)

def build_aray():
    global array
    for i in range(5000):
        array.append(rnd.randint(1,5000))
if __name__ == '__main__':        
    build_aray()
    mainTimer_Start = time.perf_counter()
    t = Process(target=doBubbleSort, daemon=True)
    x = Process(target=doSelectionSort, daemon=True)
    print('treaded')
    processes.append(t)
    processes.append(x)
    
    
    

# Start array
for process in processes:
    processes[1].start()
for process in processes:
     processes[1].join()  
    
mainTimer_Stop = time.perf_counter()   
totalTime = mainTimer_Stop - mainTimer_Start

# display BubleArray    
print('bubble sort time : '+str(bubbleTimer))
# print(BubleArray)
# display selection array
print('Selection sort time : '+str(SelectionTimer))
# print(SelectionArray)
print('Main time : ' + str(totalTime))