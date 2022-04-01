#collections.namedtuple()
#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

count = int(input())
headers = input().split()

data = namedtuple('data',headers)

total = 0
for i in range(count):
    r = input().split()
    d = data(*r)
    total += int(d.MARKS)

print(total/count)