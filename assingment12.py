#Q.1 create a thread and sleep it and then print a msg
import threading
from threading import Thread
import time
def display():
    time.sleep(5)
    print("hello world")
t=Thread(target=display)
t.start()
#Q.2.Make a thread and print number 1-10 and wait 1 sec between.
import threading
from threading import Thread
import time
def counting():
    for i in range (1,11):
     print(i)
     time.sleep(1)
s=Thread(target=counting)
s.start()

#Q.3.make a list of 5 element and print it on respectively delay
import threading
from threading import Thread
import time
l=[2,4,6,8,10]

def list():
    n = 2
    for x in l:

        if n%2==0:
         time.sleep(n)
        print(threading.current_thread().getName(), ":", x)
        n=n+2

t = Thread(target=list)
t.setName("Number")
t.start()
#Q.4.Call Factorial function Using Thread.
import threading
from threading import Thread
import time
def factorial():
    num=int(input("enter a number"))

    fact=1
    while  num>=1:
        fact=fact*num
        num=num-1
    print(fact)
    
f=Thread(target=factorial)
f.start()

 
