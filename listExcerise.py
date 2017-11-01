#addition of 2 lists
list1=[2,4,6,8]
list2=[10,20,30,40]
list3=[]
for i in range(0,len(list1)):
    list3.append((list1[i])+list2[i])
print(list3)

list4=[2,4,6,8,10,12]
list5=[10,20,30,40]
list6=[]
l1=len(list4)
l2=len(list5)
iterator=0
if l1>l2:
    iterator=l1
else:
    iterator=l2

for i in range(0,iterator):
    if (i<l1 and i<l2):
        list6.append(list4[i]+list5[i])
    elif (i<l1 and i>l2):
        list6.append(list4[i])
    else:
        list6.append(list4[i])
print(list6)
