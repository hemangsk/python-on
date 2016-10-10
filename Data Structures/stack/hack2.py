# your code goes here
import sys

def fact(n):
    f = 1
    if(n <=1):
        return n
    while(n!=1):
        f = f*n
        n = n - 1
    return f

n = sys.stdin.readlines()
i=0
times = int(n[0])

while(i < times):
    i = i + 1
    m = int(n[i])
    res = str(fact(int(n[i])))
    #print res
    l = list(res)
    l.reverse()
    count = 0
    for x in l:
        if x=='0':
            count = count + 1
        else:
            break
    print count
