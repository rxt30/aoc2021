from bingoField import BingoField

def readFile(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    playSequence = lines[0].split(",")
    playSequence = [int(num) for num in playSequence]
    playFields = []
    for i in range(2,len(lines)-1,6):
        currentField = BingoField()
        for j in range(0,5):
            currentField.addRow(lines[i+j].split())
        playFields.append(currentField)
        
    return playSequence, playFields
