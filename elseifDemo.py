# program to check biggest of 3 numbers
a=int(input("Enter first num"))
b=int(input("Enter sec num"))
c=int(input("Enter third num"))

if a>b and a>c:
    print("First num is big number")
elif b>a and b>c:
    print("Sec num is big number")
elif c>a and c>b:
    print("Third num is big number")
else:
    print("all numbers are equal")

#program to check char is vowel or not
#program1
d=str(input("Enter the charter"))
if ((d>='a' and d<='z') or (d>='A' and d<='Z')):
    if d=='a':
        print("char is Vowel")
    elif d=='e':
        print("char is Vowel")
    elif d=='i':
        print("char is Vowel")
    elif d=='o':
        print("char is Vowel")
    elif d=='u':
        print("char is Vowel")
    else:
        print("char is Consonant")
else:
    print("Entered value is not character")

#program2
if ((d>='a' and d<='z') or (d>='A' and d<='Z')):
    if(d=='a,e,i,o,u'):
        print("char is Vowel")
    else:
        print("char is Consonant")
else:
    print("Entered value is not character")

#program3
if ((d>='a' and d<='z') or (d>='A' and d<='Z')):
    if(d=='a' or d=='e' or d=='i' or d=='o' or d=='u'):
        print("char is Vowel")
    else:
        print("char is Consonant")
else:
    print("Entered value is not character")