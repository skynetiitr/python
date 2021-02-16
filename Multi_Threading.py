from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

a = Hello()
b = Hi()

a.start()
sleep(.1)
b.start()

a.join()
b.join()
print("Bye")
