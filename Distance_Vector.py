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

for i in range(lineCount):
# interates through the number rows
    for j in range(3):
    # iterates through the number of columns
    # double loop allows us to initialize the double array
        vector[i][j] = fileArray[j + i * 3]

def main():
    global vector
    
    for i in range(len(vector)):
    # adds a node to the node array
        if vector[i][0] not in nodeArray:
            nodeArray.append(vector[i][0])
        if vector[i][1] not in nodeArray:
            nodeArray.append(vector[i][1])

    for i in range(len(nodeArray)):
    # adds the current node to current node distance to the vector
    # i.e. A to A with distance 0
        vector.append([nodeArray[i], nodeArray[i], 0])

    for i in range(len(vector)):
    # iterates through our list of nodes to compare
        for j in range(len(vector)):
        # iterates through our list of nodes looking
        # to compare neighbors
            if vector[j][1] == vector[i][0] and vector[j][0] != vector[i][1]:
                decDist = (Decimal(vector[i][2]) + Decimal(vector[j][2]))
                decDist = round(decDist, 1) # round to one decimal place
                decDist = float(decDist)
                vector.append([vector[j][0], vector[i][1], decDist])
                vector.append([vector[i][1], vector[j][0], decDist])

    vector.sort()

    newList = []
    for i in range(len(nodeArray)):
    # traverse through the list of nodes
        for j in range(len(nodeArray)):
        # traverse through the list of nodes and add them as distance 1000
        # this is so duplicates node distances will be removed and the
        # left over node paths of 1000 can be changed to N/R
            vector.append([nodeArray[i], nodeArray[j], 1000])

    vector.sort()
    for i in vector:
    # iterates through our list looking for
    # matches to remove
        if i not in newList:
            newList.append(i)

    vector = newList
    for i in range(len(vector)):
    # iterates through the list of nodes to compare
        for j in range(len(vector)):
        # iterates through the list of nodes
        # to find and compare shortest path
            if i != j and (vector[i][0] == vector[j][0] and vector[i][1] == vector[j][1]):
                if vector[i][2] > vector[j][2]:
                    toRemove.append([vector[i][0], vector[i][1], vector[i][2]])
                elif vector[j][2] > vector[i][2]:
                    toRemove.append([vector[j][0], vector[j][1], vector[j][2]])

    for i in range(len(toRemove)):
    # iterates through the number of expensive traversals
    # and removes them
        if toRemove[i] in vector:
            vector.remove(toRemove[i]) 

    for i in range(len(vector)):
    # iterate through the list of nodes
    # changing the not reachable nodes to N/R
        if vector[i][2] == 1000:
            vector[i][2] = 'N/R'

    for i in range(len(nodeArray)):
    # iterates through our node list and prints the node
        print (' ')
        print ("Node: " + nodeArray[i])
        for j in range(len(nodeArray)):
        # double loops so we can print the correct nodes and values
            print ("Distance from " + str(vector[j + i * len(nodeArray)][0]) + " to " + str(vector[j + i * len(nodeArray)][1]) + " is " + str(vector[j + i * len(nodeArray)][2]))
    
if __name__ == '__main__':
    main()
