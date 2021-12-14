import numpy as np

def readInput(fileName):
    content = open(fileName).read().splitlines()
    startString = content[0]
    countDictionary = {}
    insertionDictionary = {}
    for i in range(2, len(content)):
        splitItem = content[i].split(" -> ")
        countDictionary[splitItem[0]] = 0
        insertionDictionary[splitItem[0]] = splitItem[1]
    for i in range(0, len(startString)-1):
        countDictionary[startString[i:i+2]] += 1
    return countDictionary, insertionDictionary

def getUniqueCharacters(insertionDictionary):
    uniqueCharacters = []
    for item in insertionDictionary.values():
        if item not in uniqueCharacters:
            uniqueCharacters.append(item)
    return uniqueCharacters

def updateCountDictionary(countDictionary, insertionDictionary):
    newCountDictionary = countDictionary.copy()
    for key in newCountDictionary.keys():
        newCountDictionary[key] = 0
    for key, item in countDictionary.items():
        appendChar = insertionDictionary[key]
        newCountDictionary[key[0]+appendChar] += item
        newCountDictionary[appendChar+key[1]] += item
    return newCountDictionary


def getFirstSolution(countDictionary, insertionDictionary, steps):
    for i in range(1,steps+1):
        print("Step " + str(i))
        countDictionary = updateCountDictionary(countDictionary, insertionDictionary)
        totalLength = 0
        for item in countDictionary.values():
            totalLength += item
    charactersCount = []
    for char in getUniqueCharacters(insertionDictionary):
        count = 0
        for key, item in countDictionary.items():
            if char in key:
                count += item
        count += countDictionary[char+char]
        count = (count+1) // 2
        print(charactersCount)
        charactersCount.append(count)
    return np.max(charactersCount) - np.min(charactersCount)

countDictionary, insertionDictionary = readInput("./input1401.txt")
print(getFirstSolution(countDictionary, insertionDictionary, 40))


