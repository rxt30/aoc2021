import numpy as np

class BingoField:
    def __init__(self):
        self.rows = []
        self.columns = [[],[],[],[],[]]

    def addRow(self, row):
        row = [int(num) for num in row]
        self.rows.append(row)
        for i in range(0,5):
            self.columns[i].append(row[i])

    def checkMatrix(self, drawing):
        for row in self.rows:
            if self.getEqualItems(drawing, row) == 5:
                return True, self.findUnmarked(drawing)*drawing[len(drawing)-1]

        for column in self.columns:
            if self.getEqualItems(drawing, column) == 5:
                print(column)
                return True, self.findUnmarked(drawing)*drawing[len(drawing)-1]

        return False, 0
    
    def getEqualItems(self, drawing, selfArray):
        counter = 0
        for item in selfArray:
            if item in drawing:
                counter += 1
        return counter 

    def findUnmarked(self, drawing):
        counter = 0
        for i in range(0,5):
            for j in range(0,5):
                if not self.rows[i][j] in drawing:
                    counter += self.rows[i][j]
        return counter
