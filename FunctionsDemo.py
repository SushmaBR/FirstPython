#Function with value and return value
def addNumbers(n1,n2):
    sum=n1+n2
    return sum
n1=int(input("Enter n1 Value"))
n2=int(input("Enter n2 value"))
print(addNumbers(n1,n2))
print(addNumbers(10,20))

#Function with out value and without return
def show():
    print("hi")
show()

#Function will not take anything bi=ut return sumthing
def myName():
    return "Sushma"
print(myName())

#Function take value but return nothing
def myCity(city):
    print(city)
myCity("goa")

y=2000   #global variable
def demo():
    x=1000     #local variable
    print(x)
    print(y)
    y=x+10
    print(y)
demo()
print(y)

