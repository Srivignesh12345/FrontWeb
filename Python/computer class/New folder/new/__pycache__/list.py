class grocery:
    def __init__(self,product,brand,mass):
        self.product=product
        self.brand=brand
        self.mass=mass
    def __str__(self):
        return self.product+" "+self.brand+" "+str(self.mass)