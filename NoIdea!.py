#No Idea!
#https://www.hackerrank.com/challenges/no-idea/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))


