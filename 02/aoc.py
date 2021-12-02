def readFile(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    for i in range(0,len(lines)):
        lines[i] = lines[i].split()
    return lines

def getPosition(lines):
    horizontal = 0
    depth = 0
    for line in lines:
        if line[0] == 'forward':
            horizontal += int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])
    return depth*horizontal

def getPositionSecond(lines):
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        if line[0] == 'forward':
            horizontal += int(line[1])
            depth += int(line[1])*aim
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
    return depth*horizontal

lines = readFile('./input0201.txt')
print("The solution is: " + str(getPosition(lines)))
print("The solution is: " + str(getPositionSecond(lines)))

