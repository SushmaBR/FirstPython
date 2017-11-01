x=10
y=20
z=20
print("AND Logic")
print(x > y and x > z)
print(x > y and z > x)
print(z > x and x > y)
print(z > x and y > x)
print("="*20)
print("OR Logic")
print(x > y or x > z)
print(x > y or z > x)
print(z > x or x > y)
print(z > x or y > x)
print("="*20)
print("NOT Logic")
print(not(x>y))
print(not(y>x))