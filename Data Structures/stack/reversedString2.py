n = int(input())
while(n > 0):
    n = n-1
    a = raw_input()
#    print(a)
    x,y = a.split(' ')
    x = x[::-1]
    y = y[::-1]
    res = int(x) + int(y)
    res = str(res)
    while (res[len(res)-1: len(res)] == '0') and len(res) > 0:
        res = res[:len(res)-1]
    res = res[::-1]
    print(res)
