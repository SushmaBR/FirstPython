cities=[["goa",1000],["pune",200],["ttr",1000]]
for i in cities:
    print(i)

cities.append(["nagpur",3344])
print(cities[0])
print("\n")
print(cities[1][1])
print("\n")
for row in cities:
    for e in row:
        print(e)