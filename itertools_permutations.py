#itertools.permutations()
#https://www.hackerrank.com/challenges/itertools-permutations/problem?h_r=next-challenge&h_v=zen

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')



