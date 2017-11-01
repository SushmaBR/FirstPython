a=int(input("Enter First number"))
b=int(input("Enter sec number"))
if a>b:
    print("a is bigger than b")
else:
    print("b is bigger than a")

# if both the numbers are same then else will print.. that is logical error so we are using elif
if a>b:
    print("a is bigger than b")
elif b>a:
    print("b is bigger than a")
else:
    print("a and b are equal")
    