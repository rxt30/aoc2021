from readInput import readFile
from bingoField import BingoField

def checkWin(playSequence, playFields):
    for playField in playFields:
        win, number = playField.checkMatrix(playSequence)
        if(win):
            return True, number
    return False, 0

def checkLastWin(playSequence, playFields):
    for playField in playFields:
        win, number = playField.checkMatrix(playSequence)
        if(win) and len(playFields) != 1:
            playFields.remove(playField)
        elif(win) and len(playFields) == 1:
            return True, number, playFields
    return False, 0, playFields

def findWinner(playSequence, playFields):
    for i in range(5,len(playSequence)):
        winFound, number = checkWin(playSequence[0:i], playFields)
        if(winFound):
            return number
    return 'nothing else matters'

def findLastWinner(playSequence, playFields):
    for i in range(5,len(playSequence)):
        lastWinFound, number, playFields = checkLastWin(playSequence[0:i], playFields)
        if(lastWinFound):
            return number
    return 'nothing else matters'

playSequence, playFields = readFile('./input0401.txt')
print("The number is: " + str(findWinner(playSequence, playFields)))
print("The number is: " + str(findLastWinner(playSequence, playFields)))
