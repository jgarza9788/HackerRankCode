#collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

t = int(input())
s = map(int,input().split())

myCounter =  Counter(s)

# print(myCounter)
# myCounter[5] -= 1
# print(myCounter)

cust = int(input())

total = 0
for c in range(cust):
    raw = input().split()
    print(raw)
    size = int(raw[0])
    cost = int(raw[1])
    if size in myCounter:
        total += cost
        myCounter[size] -= 1
    print(myCounter)

print(total)

