x=int(input("Enter the 6 digit number"))
n1=int((x/100000) % 10)
n2=int((x/10000) % 10)
n3=int((x/1000) % 10)
n4=int((x/100) % 10)
n5=int((x/10) % 10)
n6=x % 10
print("6 digit number is divided into digits",n1,n2,n3,n4,n5,n6)
