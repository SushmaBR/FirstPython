class A:
    def Display(self):
        print("Display method in class A")

class B(A):
    def __init__(self):
        print("Object B is created")

    def Display(self):
        super().Display()
        print("Modified display methos in class B")

b=B()
b.Display()


#overriding can be done in class