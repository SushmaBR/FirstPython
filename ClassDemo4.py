class Student:
    names=[]              #all instances will share this, if we specify inside the constructor oly perticular object will share this
    def __init__(self,n):
        print("Hi")
        self.name=n

    def ShowName(self):
        print("Student name is ",self.name)

s1=Student("Raju")
s1.ShowName()
s1.names.append(s1.name)

s2=Student("Ramu")
s2.ShowName()
s2.names.append(s2.name)
print(s1.names)
print(s2.names)
