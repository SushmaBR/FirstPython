def printAll(*n):
    for i in n:
        print(i)

printAll(10,20,30)

#functiona to add 2 numbers passed
def addAll(*n):
    sum=0
    for i in n:
        sum+=i
    return sum

print(addAll(1,2,5))
print(addAll(1,2))
print(addAll())

#taking input from array and adding it
def addArr(n):
    sum=0
    for i in n:
        sum+=i
    return sum

num=[]
x=10
while x!=0:
    x=int(input("Enter the number(0 to stop)"))
    num.append(x)
print(addArr(num))