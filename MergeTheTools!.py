#Merge the Tools!
#https://www.hackerrank.com/challenges/merge-the-tools/forum



def merge_the_tools0(string, k):
    i = 0 
    while i < len(string):
        s = string[i:][:k]
        fs = ''
        for l in s:
            if l in fs:
                pass
            else:
                fs = fs+l
        print(fs)
        i+=k

def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        # print(part)
        d = dict()
        # print(d)
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':
    # string, k = input(), int(input())
    string, k = 'AAAAAAADA', 1
    # merge_the_tools0(string, k)
    merge_the_tools(string, k)