import numpy as np

def readFile(fileName):
    lines = open(fileName, 'r').read().splitlines()[0].split(',')
    crabs = np.sort(np.array([int(num) for num in lines]))
    return crabs

def getShortestPath(crabs):
    fuelUsed = 0

    for crab in crabs:
        fuelUsed += np.sum(np.arange(0,abs(crab)))
        #Uncomment for first solution
        #fuelUsed += abs(crab)
    for i in range(crabs[0], crabs[len(crabs)-1]+1):
        newFuel = 0
        lowerFuel = True
        for crab in crabs:
            newFuel += np.sum(np.arange(0,abs(i-crab)+1))
            #Uncomment for first solution
            #fuelUsed += abs(crab-i)
            if newFuel > fuelUsed:
                lowerFuel = False
                break
        if lowerFuel:
            fuelUsed = newFuel
    return fuelUsed

crabs = readFile('./input0701.txt')
print("The number is: " + str(getShortestPath(crabs)))
