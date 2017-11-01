print("Hello World")
x=10
print(x)
print("hello\n"*5)
name1="ram"
print("%s said \"I am going to movie\"" %name1)
name2="laxman"
print("%s and %s are brothers" %(name1,name2))
age=20
height=5.8
print("my name is %s , my age is %s and my height is %s" %(name1,age,height))
print("name is " +name1)
print("one\ntwo\nthree")
print("_"*10)
print("one\ttwo\tthree")
print(name1+"\n"+name2+"\n"+str(age)+"\n"+str(height))
flexi="%s %s"
print(flexi%(name1,name2))
print(flexi%(age,name2))
print(flexi%("raja","rani"))
print(flexi%(True,False))
print(flexi%(10,20))
print(flexi%(flexi,flexi))
print("%s\n\n\n\n\n%s"%(name1,name2))
print("%s%s%s"%("ram","\n"*5,"laxman"))
print("%s%s%s"%(name1,"\n"*5,name2))