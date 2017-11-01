class Demo:
    num=0
    def __init__(self,n):    # its a constructor to class, if we are nt passing any valu then its a default consructor
        self.num=n
        print("init called")
    def ShowNum(self):
        print("Value of Num is ",str(self.num))

d1=Demo(100)
d1.ShowNum()

class Car:
    brand=""
    price=0

    def __init__(self,b,p):
        self.brand=b
        self.price=p

    def ShowDetails(self):
        print("The brand is "+self.brand+" and price is "+str(self.price))

alto=Car("maruti",500000)
alto.ShowDetails()