#itertools.product()
#https://www.hackerrank.com/challenges/itertools-product/problem

import itertools

if __name__ == '__main__':
    # string, k = input(), int(input())
    # string, k = 'AAAAAAADA', 1
    # merge_the_tools0(string, k)
    # merge_the_tools(string, k)
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # A = map(tuple,input().split())
    # B = map(tuple,input().split())
    print('A',*A)
    print('B',*B)
    # t = tuple(A,B)
    # print(t)
    l = itertools.product(A,B)
    print(*l)
    # print([((x,y) for x in A for y in B)])

