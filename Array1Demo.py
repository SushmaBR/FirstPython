arr=[1,2,2,4]

print(arr.append(5))
arr.append(6)
arr.append("sushma")
arr.append(True)
for i in arr:
    print(i)
print(arr.count(2))
print(arr.count("sushma"))
print(arr.index("sushma"))
print(arr[4]) #print the value present at index 4 and index starts from 0
arr.insert(3,20)   # index,value
print("20 is at the location",arr.index(20))
for i in arr:
    print(i)
arr.pop((arr.index("sushma")))    #it will remove the element from array
#arr.pop(arr.index(True))
for i in arr:
    print(i)
arr.reverse()
for i in arr:
    print(i)
arr.remove(6)
for i in arr:
    print(i)