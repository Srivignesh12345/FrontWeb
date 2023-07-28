class myapp:
    def __init__(self,number,nominee,period,members,sumassure):
        self.number=number
        self.nominee=nominee
        self.period=period
        self.sumassure=sumassure
        self.members=members
    def __str__(self):
        return str(self.number)+" "+self.nominee+" "+str(self.period)+"years  "+str(self.members)+"  Rs. "+ str(self.sumassure)
    