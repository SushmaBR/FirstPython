class Vehicle:
    def __init__(self,c,p):
        self.color=c
        self.price=p

class Car(Vehicle):
    def __init__(self,c,p,t):
        super().__init__(c,p)
        self.numOfTyres=t

class Bike(Vehicle):
    def __init__(self,c,p,t):
        super().__init__(c,p)
        self.numOfTyres=t

b=Bike("red",60000,2)
c=Car("red",600000,4)

print(b.color)
print(b.price)
print(b.numOfTyres)

print(c.color)
print(c.price)
print(c.numOfTyres)