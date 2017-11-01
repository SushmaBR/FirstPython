"""
def add(n1,n2):
    sum=n1+n2
    return sum
result=add(10,20)
"""

result=lambda n1,n2:n1+n2
print(result(10,20))

#to calculate square
square=lambda n1:n1**2
#square=lambda n1:n1*n1   both the functionalities will work
print(square(10))

#To calculate cube
cube=lambda n1:n1**3
#cube=lambda n1:n1*n1*n1
print(cube(10))

#upperlower
upperAndLower=lambda str:str.upper()+str.lower()
print(upperAndLower("sushma"))