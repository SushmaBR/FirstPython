name=" "
namesFile=open('names.txt','a')
while(name!='end'):
    name=input("Enter the name")
    if(name=='end'):
        break
    namesFile.write(name+'\n')
namesFile.close()

namesFile=open('names.txt','r')
names=namesFile.readlines()
namesFile.close()

for n in names:
    print(n)
