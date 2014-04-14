# Project 3
# Joel Scott
# jascott@uga.edu

from decimal import *

file = input('Please choose file:')

lineCount = 0
fileArray = []
nodeArray = []

myFile = open(file + '.txt', 'r')
for line in myFile:
# reads one line of the file and
# breaks into chunks as start, neighbor, distance
    lineCount = lineCount + 2
    a, b, c = [i for i in line.split()]
    c = float(c)
    fileArray.append(a)
    fileArray.append(b)
    fileArray.append(c)
    fileArray.append(b)
    fileArray.append(a)
    fileArray.append(c)

vector = [[0 for x in range(3)] for x in range(lineCount)]
newList = []
toRemove = []
x = len(vector)
y = x + 1

for i in range(lineCount):
# interates through the number rows
    for j in range(3):
    # iterates through the number of columns
    # double loop allows us to initialize the double array
        vector[i][j] = fileArray[j + i * 3]

    
def main():
    global vector, x, y
    
#    print (vector)
    for i in range(len(vector)):
        if vector[i][0] not in nodeArray:
            nodeArray.append(vector[i][0])
        if vector[i][1] not in nodeArray:
            nodeArray.append(vector[i][1])

    for i in range(len(nodeArray)):
        vector.append([nodeArray[i], nodeArray[i], 0])


    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[j][1] == vector[i][0] and vector[j][0] != vector[i][1]:
                decDist = (Decimal(vector[i][2]) + Decimal(vector[j][2]))
                decDist = round(decDist, 1) # round to one decimal place
                decDist = float(decDist)
                vector.append([vector[j][0], vector[i][1], decDist])
                vector.append([vector[i][1], vector[j][0], decDist])

    vector.sort()

    newList = []
    for i in vector:
        if i not in newList:
            newList.append(i)
            
    vector = newList

    for i in range(len(vector)):
        for j in range(len(vector)):
            if i != j and (vector[i][0] == vector[j][0] and vector[i][1] == vector[j][1]):
                if vector[i][2] > vector[j][2]:
                    toRemove.append([vector[i][0], vector[i][1], vector[i][2]])
                elif vector[j][2] > vector[i][2]:
                    toRemove.append([vector[j][0], vector[j][1], vector[j][2]])

    for i in range(len(toRemove)):
        if toRemove[i] in vector:
            vector.remove(toRemove[i])

    for i in range(len(nodeArray)):
        print ("Node: " + nodeArray[i])
        print ("Distance from " + str(vector[6 * i][0]) + " to " + str(vector[6 * i][1]) + " is " + str(vector[6 * i][2]))
        print ("Distance from " + str(vector[6 * i + 1][0]) + " to " + str(vector[6 * i + 1][1]) + " is " + str(vector[6 * i + 1][2]))
        print ("Distance from " + str(vector[6 * i + 2][0]) + " to " + str(vector[6 * i + 2][1]) + " is " + str(vector[6 * i + 2][2]))
        print ("Distance from " + str(vector[6 * i + 3][0]) + " to " + str(vector[6 * i + 3][1]) + " is " + str(vector[6 * i + 3][2]))
        print ("Distance from " + str(vector[6 * i + 4][0]) + " to " + str(vector[6 * i + 4][1]) + " is " + str(vector[6 * i + 4][2]))
        print ("Distance from " + str(vector[6 * i + 5][0]) + " to " + str(vector[6 * i + 5][1]) + " is " + str(vector[6 * i + 5][2]))
        print (' ')


    
    
if __name__ == '__main__':
    main()
