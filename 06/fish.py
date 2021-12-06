import numpy as np
def readFile(fileName): 
    lines = open(fileName, 'r').read().splitlines()[0].split(',')
    fishes = np.array([int(num) for num in lines])
    return fishes

def getFishCount(fishes, days):
    fishCounter = np.zeros(9)
    for fish in fishes:
        fishCounter[fish] += 1 
    for i in range(0, days):
        zeros = fishCounter[0]
        for i in range(1, 9):
            fishCounter[i-1] = fishCounter[i]
        fishCounter[8] = zeros
        fishCounter[6] += zeros
    return np.sum(fishCounter)

fishes = readFile('./input0601.txt')
print("The first solution is: " + str(getFishCount(fishes, 80)))
print("The second solution is: " + str(getFishCount(fishes, 256)))
