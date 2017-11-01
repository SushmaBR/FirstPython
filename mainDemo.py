name="Ram"
def fun1(x):
    print(name)
    print("before mod in fun1:",x)
    x=100 #modifying fun1.x instead of main.x
    print("after mod in fun1",x)

def main():
    print("Hi")
    print(name)
    x=20
    fun1(x)
    print("x value in main",x)  #value of x is not 100 coz we mod fun1.x not main.x

main()