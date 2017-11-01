class A:
    def __init__(self):
        self.x=10

class B(A):
    def __init__(self):
      #  super(B, self).__init__()   both are statments are same , we ca use either one
        super().__init__()
        self.y=20

demo=B()
print(demo.x)
print(demo.y)