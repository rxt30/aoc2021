def readFile(fileName):
    coordinates = []
    lines = open(fileName, 'r').read().splitlines()
    for i in range(0,len(lines)):
        lines[i].rstrip('\n')
        coordinates.append(lines[i].split(' -> '))
        coordinates[i][0] = coordinates[i][0].split(',')
        coordinates[i][0] = [int(num) for num in coordinates[i][0]]
        coordinates[i][1] = coordinates[i][1].split(',')
        coordinates[i][1] = [int(num) for num in coordinates[i][1]]
    return coordinates

