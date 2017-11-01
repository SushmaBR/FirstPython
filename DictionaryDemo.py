d={
    1:"ramu",
    2:"ravi",
    3:"manju",
    4:"madhu"
}

for names in d:            # no need to mention .keys.. with out that also it will print keys
    print(d[names])
    print(names)
print("\n")
    #print(d.keys())

d1={
    "paris":"France",          #keys:values
    "Tokyo":"Japan",
    "Budapest":"hungary",
    "London":"England",
    "Delhi":"India",
    "Islamabad":"Pakistan"
}

for item in d1.keys():
    print(item)
    print(d1[item])
print("\n")

for item in d1.keys():
    print(item + "-" + d1[item])

for item in d1.values():
    print(item)

print("Sixe of the dictionary is", len(d1))
print(d1.keys())
print("\n")
print(d1.values())
print("\n")
print(d1.items())
print(d1["London"])  # print the value of key London
print(d1.get("London"))  # print the value of key London
del d1["Islamabad"]    # delete Islamabad
print(d1)

d1.pop("London")
print(d1)
print(len(d1))
d1.clear()
print(len(d1))