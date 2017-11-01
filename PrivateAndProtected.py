class A:
    def __init__(self):
        self.__x=10

    def _ShowX(self):
        print("showing x value from class A",self.__x)

    def Display(self):
        self._ShowX()

class B(A):
    def __init__(self):
        super().__init__()

    def Print(self):
        self._ShowX()

obja=A()
obja.Display()

objb=B()
objb.Print()

# Single underscore means protected (_ShowX) available to its and its inherited class
#Double underscore means private( __X)   available oly to its own class
#without any underscore means public