"""
x=[10,"sush",True,30,50]
x[1]=1000
for i in x:
    print(i)
print("First element is",x[0])
"""

list1=[10,20]
list2=[5,15]
list3=list1+list2   #list addition or list concatenation
#for i in list3:
print(list3)
print("list4") #[start:end+1]
list4=list3[2:4]    #taking part of list is called slicing
for i in list4:
    print(i)
print(list)
list4=list3[:4]  #taking part of list is called slicing
for i in list4:
    print(i)
print(list)
list4=list3[2:]
for i in list4:
    print(i)
print(list)
list4=list3[:]
for i in list4:
    print(i)
print("list addition")
list5=[100,200]
#list6=list5+list5
list6=list5*5   #instead of adding/concatination the list 5 times we can write like this
for i in list6:
    print(i)
print(list6)

list7=[1,2,3,4,5,6,7,8,9]
print("2 in list7:" , 2 in list7)   #give boolean value if number is present in list
print("12 in list7:", 12 in list7)

print("2 not in list7:",2 not in list7) # negation of above stattement
print("12 not in list7:",12 not in list7)

list8=[10,20,30,40,50]
print("list methods")
print(list8.count(10))
list8.append(60)
print(list8)
list8.extend(list7) # append list7 to list8
print(list8)
list8.insert(0,5)
print(list8)
list8.insert(18,500)
print(list8)
list8.remove(30)
print(list8)
list8.pop(3)   # remove value present at index 3
print(list8)
list8.pop()  #if we dont specify value, it wil remove last number
print(list8)
list8.sort()
print("sorting")
print(list8)
list8.sort(reverse=True)  #reverse sorting
print(list8)
list8.reverse()
print(list8)

list9=[x for x in list8]   # same as coping list8
print(list9)

list9=[x for x in list8 if x%5==0]    #subset of list8 having value which is divisible by 5
print(list9)

list10=[x for x in range(1,11)]
print(list10)

list11=[x**2 for x in range(1,11) if x%2==0]
print(list11)

list12=["ttr","ask","bng","paris","karnataka"]
list12=[x.upper() for x in list12 if len(x)<=4]
print(list12)

list13=[10,2,13,6,40,9]
print("size of the list is:", len(list13))
print("biggest num in the list is:", max(list13))
print("smallest number in the list is:",min(list13))
print("sum of numbers in list is",sum(list13))