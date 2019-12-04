#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen

# NM = int(input())
LM = set(map(int,input().split()))
# NN = int(input())
LN = set(map(int,input().split()))

# print(LM)
# print(LN)

result = LM.difference(LN)
# print(result)
result.update(LN.difference(LM))
# print(result,sep='\n')
for r in sorted(result, reverse=False):
    print(r)

