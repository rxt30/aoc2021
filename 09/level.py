def readFile(fileName):
    content = open(fileName).read().splitlines()
    content = [list(number) for number in content]
    content = [[int(number) for number in item] for item in content]
    content = [[9]+item+[9] for item in content]
    filler = [9 for i in range(0,len(content[0]))] 
    content = [filler] + content + [filler]
    return content

def findLows(content):
    counter = 0
    for i in range(1, len(content)-1):
        for j in range(1, len(content[0])-1):
            leftSideCheck = content[i][j-1] > content[i][j]
            rightSideCheck = content[i][j+1] > content[i][j]
            topSideCheck = content[i+1][j] > content[i][j]
            bottomSideCheck = content[i-1][j] > content[i][j]
            if leftSideCheck and rightSideCheck and topSideCheck and bottomSideCheck:
                counter += content[i][j]+1
    return counter

def findBasin(content)
    foundNumbers = []
    for i in range(1, len(content)-1):
        for j in range(1, len(content[0])-1):
            leftSideCheck = content[i][j-1] > content[i][j]
            rightSideCheck = content[i][j+1] > content[i][j]
            topSideCheck = content[i+1][j] > content[i][j]
            bottomSideCheck = content[i-1][j] > content[i][j]
            if leftSideCheck and rightSideCheck and topSideCheck and bottomSideCheck:
                foundNumbers.append(findBasinSize(foundNumbers,i,j))
    return counter

content = readFile("./input0901.txt")
print("The number is: " + str(findLows(content)))
