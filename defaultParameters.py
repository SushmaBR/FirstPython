def calculateSI(principle,time,rateOfInterest=2):    # (principle,time,rateOfInterest) we can specify like this also.. if we pass value then it will overwrite otherwise it will take default value
    si=(principle*time*rateOfInterest)/100
    return si

print(calculateSI(100,1,1))
print(calculateSI(1000,2))
print(calculateSI(principle=100,time=1,rateOfInterest=1))