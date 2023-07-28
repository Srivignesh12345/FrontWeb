from abc import ABC
class bus(ABC):
    def volvo(self):
        print("hello")
        pass
class SRT (bus):
    def volvo (self):
        print("Its a luxury bus")
class KPN(bus):
    def volvo(self):
        print("AC bus")
class SAT(bus):
    def volvo(self):
        print("luxury vehicle") 
s=SRT()
s.volvo()
s1=SAT()
s1.volvo()
b=bus()
b.volvo()   