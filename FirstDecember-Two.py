totalFuel = 0
inputFile = open('input.txt','r')

for currentMass in inputFile:
    keepGoing = True
    currentSum = 0
    mass = currentMass
    while (keepGoing):
        currentMassLong  = long(mass)
        currentfuel = (currentMassLong//3)-2
        if (currentfuel<=0):
            keepGoing = False
        else:
            mass = currentfuel
            currentSum+=currentfuel
    totalFuel+=currentSum
    
print "totalFuel: ", totalFuel
