# Used for the numbers 1,7,4,8, as they have unique amount of characters
def uniqueNumbersFind(fileContent, lengthNumber):
    for item in fileContent:
        if len(item) == lengthNumber:
            return "".join(sorted(item))
    return ""

def findThreeAndSix(fileContent, oneString, numberOfChars, FindSix):
    notMatchOneStringLength = 1 if FindSix else 0
    for item in fileContent:
        if len(item) == numberOfChars and len(set(oneString).difference(item)) == notMatchOneStringLength:
            return "".join(sorted(item))
    return "drei"

def findLeftSide(eightString, threeString):
    return "".join(sorted(set(threeString).difference(eightString)))

def findNineAndZero(fileContent, oneString, leftSideChars, findZero):
    notMatchStringLength = 0 if findZero else 1
    for item in fileContent:
        if len(item) == 6 and len(set(oneString).difference(item)) == 0 and len(set(leftSideChars).difference(item)) == notMatchStringLength:
            return "".join(sorted(item))
    return ""

def findTopLeftString(fourString, leftSideChars):
    return "".join(sorted(set(leftSideChars).difference(fourString)))

def findFiveAndTwoString(fileContent, topLeftString, oneString, findTwo):
    for item in fileContent:
        if len(item) == 5 and len(set(oneString).difference(item)) == 1 and (topLeftString in item) == findTwo:
            return "".join(sorted(item))
    return ""

def getDictionary(fileContent):
    fileContent = ["".join(sorted(item)) for item in fileContent]
    oneString = uniqueNumbersFind(fileContent, 2)
    sevenString = uniqueNumbersFind(fileContent, 3)
    fourString = uniqueNumbersFind(fileContent, 4)
    eightString = uniqueNumbersFind(fileContent, 7)
    sixString = findThreeAndSix(fileContent, oneString, 6, True)
    threeString = findThreeAndSix(fileContent, oneString, 5, False)
    leftSideChars = findLeftSide(threeString, eightString)
    nineString = findNineAndZero(fileContent, oneString, leftSideChars, False)
    zeroString = findNineAndZero(fileContent, oneString, leftSideChars, True)
    topLeftString = findTopLeftString(fourString, leftSideChars)
    fiveString = findFiveAndTwoString(fileContent, topLeftString, oneString, False)
    twoString = findFiveAndTwoString(fileContent, topLeftString, oneString, True)
    return {
            zeroString:"0",
            oneString:"1",
            twoString:"2",
            threeString:"3",
            fourString:"4",
            fiveString:"5",
            sixString:"6",
            sevenString:"7",
            eightString:"8",
            nineString:"9"
            }

