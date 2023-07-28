class sam:
    def name(self):
        print("Srivignesh")
class raja(sam):
    def name(self):
        super().name()
        print("raja")
class arun(raja):
    def name(self):
        super().name()
        print("Arun")
s=arun()
s=raja()
s=sam()
s.name()
