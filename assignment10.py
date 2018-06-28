# Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import thread #required to import the module.
import time
print("Before the sleep statement") #a message before sleep.
time.sleep(5) #a sleep of 5 seconds.
print("After the sleep statement") #a message after sleep.

# Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between
import thread #required for import the module.
import time
i=0
while i<10: #condition to xecute the loop.
    time.sleep(1) #time sleep of 1 second.
    i += 1
    print(i) #print number.

# Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of
# 2 sec between each display.Delay goes like 2sec-4sec-6sec-8sec-10sec
import thread
import time
lst = ['Sakshi','Manik','Avneet','Rinku','Sangam']
i=1
for x in lst:
    print(x)
    delay = float(2*i)
    time.sleep(delay)
    i += 1

#Q4. Call factorial function using thread.
import thread
import math
n = input("enter the no.")
fact = math.factorial(n)
print(fact)



