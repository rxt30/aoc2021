def readFile(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    for i in range(0,len(lines)):
        lines[i] = list(lines[i])
    return lines

def getPower(lines):
    gamma = ""
    epsilon = ""
    for i in range(0,len(lines[0])-1):
        oneCounter = 0
        zeroCounter = 0
        for j in range(0,len(lines)):
            if lines[j][i] == "0":
                zeroCounter += 1
            else:
                oneCounter += 1
        if zeroCounter > oneCounter:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(gamma)
    print(epsilon)
    return int(gamma, 2)*int(epsilon, 2)

def getLifeSupport(lines):
    o2rating = getO2Rating(lines)
    co2rating = getCO2Rating(lines)
    print(o2rating)
    print(co2rating)
    return o2rating*co2rating

def getO2Rating(lines):
    for i in range(0,len(lines[0])-1):
        if len(lines) == 1:
            break
        oneCounter = 0
        zeroCounter = 0
        for j in range(0,len(lines)):
            if lines[j][i] == "0":
                zeroCounter += 1
            else:
                oneCounter += 1
        if zeroCounter > oneCounter:
            lines = [item for item in lines if item[i] == '0']
        else:
            lines = [item for item in lines if item[i] == '1']
    return int("".join(lines[0]), 2)

def getCO2Rating(lines):
    for i in range(0,len(lines[0])-1):
        if len(lines) == 1:
            break
        oneCounter = 0
        zeroCounter = 0
        for j in range(0,len(lines)):
            if lines[j][i] == "0":
                zeroCounter += 1
            else:
                oneCounter += 1
        if zeroCounter <= oneCounter:
            lines = [item for item in lines if item[i] == '0']
        else:
            lines = [item for item in lines if item[i] == '1']
    return int("".join(lines[0]), 2)

lines = readFile('./input0301.txt')
print("The solution is: " + str(getPower(lines)))
print("The solution is: " + str(getLifeSupport(lines)))
