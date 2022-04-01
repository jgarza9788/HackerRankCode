#Introduction to Sets
#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


n = int(input())
nums = list(map(int,input().split()))

sum = 0
count = 0
for i in set(nums):
    sum+=i
    count +=1

print(sum/count)



