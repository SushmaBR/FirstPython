"""
num1=10
num2=0
result=num1/num2
print(result)
print("program ended normally")
"""
import sys
num1=10
num2=0
result=0
arr=[10,20,30]
try:
    result=num1/num2
except ZeroDivisionError:
    #print("some exception")
    print("Error:",sys.exc_info()[1],"occured")
finally:
    print("Finally executed for division irresptive of exception")
try:
    print(arr[5])
except IndexError:
    ob=IndexError
    print("Error:",sys.exc_info()[1],"occured")
    #print("index out of range")
finally:
    print("Finally executed for array irresptive of exception")
#print(result)
print("program ended normally")
print("\n")
try:
    limit=int(input("Enter the number"))
    if limit<1000:
        print("number is within limit")
    else:
        print("number is out of range")
        raise IndexError    #manually raised by programmer before system raising it after precheck
except IndexError:
    print("raised exception handeled")