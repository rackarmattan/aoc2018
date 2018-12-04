from collections import Counter

myfile = open('2.txt', 'r')
contents = myfile.read().strip().splitlines()
myfile.close()


c = [0, 0]
for i in contents:
    a = [j for i, j in Counter(i).most_common()]

    if 3 in a:
        c[0] += 1
    if 2 in a:
        c[1] += 1


print(c[0] * c[1])

count = 0
result = ''

for x in range(len(contents) - 1):
    tmp = contents[x]
    for y in range(x+1, len(contents), 1):
        tmp2 = contents[y]
        for z in range(len(tmp)):
            if tmp[z] == tmp2[z]:
                count += 1
                result = result + tmp[z]

                if count == (len(tmp) - 1):
                    print(result)
        result = ''
        count = 0

