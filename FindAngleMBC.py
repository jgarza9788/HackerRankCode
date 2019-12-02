#Find Angle MBC
#https://www.hackerrank.com/challenges/find-angle/problem?h_r=next-challenge&h_v=zen

import math

from random import random

A = int(input())
C = int(input())

# A = int(random() * 10)
# C = int(random() * 10)
print(A,C)

# A^2 + B^2 = C^2
# m = math.sqrt(pow(AB,2)+pow(BC,2))

mPoint = [C/2,A/2]

print(math.degrees(math.atan(mPoint[1]/mPoint[0])))
print('{:.0f}°'.format(math.degrees(math.atan(mPoint[1]/mPoint[0]))))

# hM = m/2

# print(hM)
# print(BC)

# print(math.asin(4.27/3))
# print(math.degrees(math.asin(4.27/3)))

# #sin^-1 with adj/hyp
# print(math.degrees(math.asin(hM/BC)))
# print('{:.0f}°'.format(math.degrees(math.asin(hM/BC))))
# # print('{:.0f}°'.format(56.5))
