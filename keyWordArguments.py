def calculateSI(principle,time,rateOfInterest):
    SI=(principle*time*rateOfInterest)/100
    print("Principle:",principle)
    print("Time:",time)
    print("Intrest:",rateOfInterest)
    return SI

print(calculateSI(time=2,principle=1000,rateOfInterest=1))