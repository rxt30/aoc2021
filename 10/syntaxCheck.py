import numpy as np

def readInput(filename):
    return open(filename).read().splitlines()

def getWrongBrace(content):
    illegalCharacterCounter = 0
    closingCharactersQueue = []
    illegalCharacterScores = {
            ")":3,
            "]":57,
            "}":1197,
            ">":25137
            }
    for line in content:
        for character in line:
            if character == "(":
                closingCharactersQueue.append(")")
            elif character == "[":
                closingCharactersQueue.append("]")
            elif character == "{":
                closingCharactersQueue.append("}")
            elif character == "<":
                closingCharactersQueue.append(">")
            else:
                if character == closingCharactersQueue[len(closingCharactersQueue)-1]:
                    closingCharactersQueue.pop()
                else:
                    illegalCharacterCounter += illegalCharacterScores[character]
                    break
    return illegalCharacterCounter

def autoComplete(content):
    completionScores = []
    illegalCharacterScores = {
            ")":1,
            "]":2,
            "}":3,
            ">":4
            }
    for line in content:
        engageAutoComplete = True
        closingCharactersQueue = []
        for character in line:
            if character == "(":
                closingCharactersQueue.append(")")
            elif character == "[":
                closingCharactersQueue.append("]")
            elif character == "{":
                closingCharactersQueue.append("}")
            elif character == "<":
                closingCharactersQueue.append(">")
            else:
                if character == closingCharactersQueue[len(closingCharactersQueue)-1]:
                    closingCharactersQueue.pop()
                else:
                    engageAutoComplete = False
                    break
        if engageAutoComplete:
            lineScore = 0
            closingCharactersQueue.reverse()
            for items in closingCharactersQueue:
                lineScore = (lineScore*5) + illegalCharacterScores[items]
            completionScores.append(lineScore)
    return np.take(np.sort(completionScores), len(completionScores) // 2)


content = readInput('./input1001.txt')
print("The first score is : " + str(getWrongBrace(content)))
print("The second score is : " + str(autoComplete(content)))

