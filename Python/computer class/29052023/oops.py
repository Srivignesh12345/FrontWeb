#basic concept of oops
class college:
    def __init__(self,name,course):
        self.n=name
        self.c=course
    def print(self):
        print(self.n,self.c)
c=college("Sri Eshwar",2023)
c.print()            
        