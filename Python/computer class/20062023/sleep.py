from threading import *
from time import sleep
class React(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
        self.click=[12,23,34,45,56,67,78,89,23,]
    def run(self):
        print("Welcome",self.name)
        for x in self.click:
            print(x)
            sleep(2)
r1=React("Srivignesh")
r2=React("Sri")
r3=React("Vignesh")


r1.start()
r1.join()
r2.start()
r2.join()
r3.start()
r3.join()