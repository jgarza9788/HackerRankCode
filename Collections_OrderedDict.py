#Collections.OrderedDict()
#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?h_r=next-challenge&h_v=zen

from collections import OrderedDict

OD = OrderedDict()


def splitNameNum(string):
    result = []
    for i in range(len(string)):
        # print(string[i:])
        if string[i:].isnumeric():
            result.append(string[:i].strip())
            result.append(int(string[i:].strip()))
            break
    return result

N = int(input())

for i in range(N):
    # print(i)
    # print(splitNameNum(input()))
    NN = splitNameNum(input())
    if NN[0] in OD:
        OD[NN[0]] += NN[1]    
    else:
        OD[NN[0]] = NN[1]


for key, value in OD.items(): 
    print(key, value) 