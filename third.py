import numpy

myfile = open('3.txt', 'r')
contents = myfile.read().strip().splitlines()
myfile.close()

def matrixSize():
    matrixHeight = 0
    matrixWidth = 0
    for x in contents:
        leftPointer = 0
        rightPointer = 0
        while x[leftPointer] != ' ':
            leftPointer += 1

        leftPointer = leftPointer + 3
        rightPointer = leftPointer

        while x[rightPointer] != ',':
            rightPointer += 1

        # hur långt från vänster den ska börrja
        leftMargin = int(x[leftPointer:rightPointer])

        # print('left margin: ', leftMargin)

        rightPointer += 1
        leftPointer = rightPointer

        while x[rightPointer] != ':':
            rightPointer += 1

        # hur långt från toppen den ska börja
        topMargin = int(x[leftPointer:rightPointer])
        # print('top margin ', topMargin)

        rightPointer += 2
        leftPointer = rightPointer

        while x[rightPointer] != 'x':
            rightPointer += 1

        width = int(x[leftPointer:rightPointer])

        # print('width ', width)

        rightPointer += 1
        leftPointer = rightPointer

        height = int(x[leftPointer:len(x)])

        if leftMargin + width > matrixWidth:
            matrixWidth = leftMargin + width
        if topMargin + height > matrixHeight:
            matrixHeight = topMargin + height

    return(matrixWidth, matrixHeight)


matrix = numpy.zeros(matrixSize())

for x in contents:
    leftPointer = 0
    rightPointer = 0
    while x[leftPointer] != ' ':
        leftPointer += 1

    leftPointer = leftPointer + 3
    rightPointer = leftPointer

    while x[rightPointer] != ',':
        rightPointer += 1

    # hur långt från vänster den ska börrja
    leftMargin = int(x[leftPointer:rightPointer])


    rightPointer += 1
    leftPointer = rightPointer

    while x[rightPointer] != ':':
        rightPointer += 1

    # hur långt från toppen den ska börja
    topMargin = int(x[leftPointer:rightPointer])

    rightPointer += 2
    leftPointer = rightPointer

    while x[rightPointer] != 'x':
        rightPointer += 1

    width = int(x[leftPointer:rightPointer])

    rightPointer += 1
    leftPointer = rightPointer

    height = int(x[leftPointer:len(x)])

    for row in range(topMargin, topMargin + height, 1):
        for col in range(leftMargin, leftMargin + width, 1):
           matrix[row, col] += 1

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] >= 2:
            count += 1
print(count)



