file = open('1.txt', 'r')

result = 0
strlist = []
resultlist = []

for line in file:
    strlist.append(line)

go = True

while go:
    for i in range(len(strlist)):
        result += int(strlist[i])

        if result in resultlist:
            print(result)
            go = False
            break
        else:
            resultlist.append(result)



