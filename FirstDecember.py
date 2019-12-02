sum = 0
inputFile = open('input.txt','r')
for currentMass in inputFile:
    currentMassLong  = long(currentMass.strip())
    currentfuel = (currentMassLong//3)-2
    sum+=currentfuel
print "sum: ", sum