# Project 3
# Joel Scott
# jascott@uga.edu

file = input('Please choose file:')

lineCount = 0
fileArray = []

myFile = open(file + '.txt', 'r')
for line in myFile:
# reads one line of the file and
# breaks into chunks as start, neighbor, distance
    lineCount = lineCount + 1
    a, b, c = [i for i in line.split()]
    c = float(c)
    fileArray.append(a)
    fileArray.append(b)
    fileArray.append(c)

vector = [[0 for x in range(3)] for x in range(lineCount)]
i = 0
j = 0
for i in range(lineCount):
# interates through the number rows
    for j in range(3):
    # iterates through the number of columns
        vector[i][j] = fileArray[j + i * 3]

    
def main():
    print (vector)
    
if __name__ == '__main__':
    main()
