from readInput import readFile
import numpy as np

def findBiggestCoordinates(coordinates):
    x,y = 0,0
    for coordinate in coordinates:
        if int(coordinate[0][0]) > x:
            x = int(coordinate[0][0])
        elif coordinate[1][0] > x:
            x = coordinate[1][0]

        if coordinate[0][1] > y:
            y = coordinate[0][1]
        elif coordinate[1][1] > y:
            y = coordinate[1][1]
    return x,y

def getBadLinesCounter(coordinates):
    counter = 0 
    for coordinate in coordinates:
        for item in coordinate:
            if item >= 2:
                counter += 1
    return counter

def findBadLines(coordinates, xMax, yMax):
    initialField = np.zeros((xMax+1, yMax+1))
    for coordinate in coordinates:
        if coordinate[0][0] == coordinate[1][0]:
            fixedPosition = coordinate[0][0]
            bigger = coordinate[0][1] if coordinate[0][1] > coordinate[1][1] else coordinate[1][1] 
            smaller = coordinate[1][1] if coordinate[0][1] > coordinate[1][1] else coordinate[0][1] 
            for i in range(smaller, bigger+1):
                initialField[fixedPosition][i] += 1
        elif coordinate[0][1] == coordinate[1][1]:
            fixedPosition = coordinate[0][1]
            bigger = coordinate[0][0] if coordinate[0][0] > coordinate[1][0] else coordinate[1][0] 
            smaller = coordinate[1][0] if coordinate[0][0] > coordinate[1][0] else coordinate[0][0] 
            for i in range(smaller, bigger+1):
                initialField[i][fixedPosition] += 1
        #comment this for first solution
        else:
            biggerX = coordinate[0][0] if coordinate[0][0] > coordinate[1][0] else coordinate[1][0] 
            smallerX = coordinate[1][0] if coordinate[0][0] > coordinate[1][0] else coordinate[0][0] 
            xFalling = True if coordinate[0][0] > coordinate[1][0] else False 
            smallerY = coordinate[1][1] if coordinate[0][1] > coordinate[1][1] else coordinate[0][1] 
            yFalling = True if coordinate[0][1] > coordinate[1][1] else False
            if xFalling == yFalling:
                for i in range(0, biggerX-smallerX+1):
                    initialField[smallerX+i][smallerY+i] += 1
            else:
                for i in range(0, biggerX-smallerX+1):
                    initialField[biggerX-i][smallerY+i] += 1
        # got a problem if x is rising and y falling


    print(initialField)
    return getBadLinesCounter(initialField)

coordinates = readFile('./input0501.txt')
xMax, yMax = findBiggestCoordinates(coordinates)
print("The number is " + str(findBadLines(coordinates, xMax, yMax)))
