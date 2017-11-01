for i in range (1,11):
    if i==5:
        continue
    if i==7:
        break
    print(i)

#one more example for break and continue
#program to search key in a array
arr=[10,20,30,40,50,60]
found=False
key=int(input("Enter the value to be searched"))
for i in arr:
    if i==key:
        found=True
        break
if found==True:
    print("key found")
else:
    print("key is not found")