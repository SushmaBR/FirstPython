str1=['s','u','s','h']
str2="sush"
print(str1)
print(str2)
print(str1[1])
print(str2[1])

msg="python is flexible programming language python"
print(msg[7:11])
print(msg.index("flexible"))
print(msg[msg.index("flexible"):msg.index("flexible")+10])
print(msg[:-10]) #remove last 10 characters
print(msg[-10:]) #give last 10 characters
print(msg[0:7]+"-I will learn")  # it will take frst 6 characters and it will append "i will learn
print(msg.capitalize())   # it will capitalize forst character
print(msg.upper())   # change all characters to upper case
print(msg.index("programming"))
str1='1KI07EC051'
str="sushma"
print(str1.isalpha())
print(str1.isalnum())
print(msg.isalpha())
print(str.isalpha())
print(msg.replace("python","java",1))  #for self  no need to specify anything
str3="    hi    "
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())

