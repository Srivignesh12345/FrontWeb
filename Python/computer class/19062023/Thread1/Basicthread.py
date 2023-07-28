from threading import *

class Fiesta(Thread):
    def __init__(self,nm = ""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcome",self.name)
f1=Fiesta("vicky")
f2=Fiesta("sri")
f3=Fiesta("mathi")
f1.start()
f2.start()
f3.start()