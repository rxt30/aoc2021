from getDictionary import getDictionary

def readInput(filename):
    content = open(filename).readlines()
    content = [name.split() for name in content]
    return content

def firstSolution(content):
    counter = 0
    for item in content:
        for i in range(len(item)-4, len(item)):
            if len(item[i]) == 2 or len(item[i]) == 3 or len(item[i]) == 4 or len(item[i]) == 7:
                counter += 1
    return counter

def secondSolution(content):
    totalSum = 0
    for item in content:
        numberString = ""
        dict = getDictionary(item)
        for i in range(len(item)-4, len(item)):
            currentItem = str(item[i])
            numberString += dict["".join(sorted(currentItem))]
        totalSum += int(numberString)
    return totalSum

content = readInput("./input0801.txt")
print("The first solution is: " + str(firstSolution(content)))
print("The second solution is: " + str(secondSolution(content)))
