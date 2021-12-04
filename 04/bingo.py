from readInput import readFile
from bingoField import BingoField

def checkWin(playSequence, playFields):
    for playField in playFields:
        win, number = playField.checkMatrix(playSequence)
        if(win):
            return True, number
    return False, 0

def findWinner(playSequence, playFields):
    for i in range(5,len(playSequence)):
        winFound, number = checkWin(playSequence[0:i], playFields)
        if(winFound):
            return number
    return 'nothing else matters'

playSequence, playFields = readFile('./input0401.txt')
print("The number is: " + str(findWinner(playSequence, playFields)))
