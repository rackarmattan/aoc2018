import numpy

myfile = open('3.txt', 'r')
contents = myfile.read().strip().splitlines()
myfile.close()

def marginLeft(x):
    return int(x[x.find(' ')+2:x.find(',')])

def marginTop(x):
    return int(x[x.find(',')+1:x.find(':')])

def get_width(x):
    return int(x[x.find(':') + 2:x.find('x')])

def get_height(x):
    return int(x[x.find('x')+1:len(x)])

def get_id(x):
    return int(x[1:x.find(' ')])

def matrixSize():
    matrixHeight = 0
    matrixWidth = 0
    for x in contents:

        if marginLeft(x) + get_width(x) > matrixWidth:
            matrixWidth = marginLeft(x) + get_width(x)
        if marginTop(x) + get_height(x) > matrixHeight:
            matrixHeight = marginTop(x) + get_height(x)

    return(matrixWidth, matrixHeight)

matrix = numpy.zeros(matrixSize())

for x in contents:

    id = get_id(x)

    leftMargin = marginLeft(x)

    topMargin = marginTop(x)

    width = get_width(x)

    height = get_height(x)

    for row in range(topMargin, topMargin + height, 1):
        for col in range(leftMargin, leftMargin + width, 1):
           matrix[row, col] += 1

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] >= 2:
            count += 1
print(count)


for x in contents:
    id = get_id(x)

    leftMargin = marginLeft(x)

    topMargin = marginTop(x)

    width = get_width(x)

    height = get_height(x)

    area = width*height
    checkArea = 0

    for row in range(topMargin, topMargin + height, 1):
        for col in range(leftMargin, leftMargin + width, 1):
            checkArea += matrix[row][col]

    if checkArea == area:
        print(id)
        break



