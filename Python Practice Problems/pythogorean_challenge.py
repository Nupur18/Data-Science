import math
t = eval(input())

while(t):
    n = eval(input())
    for a in range(int(math.sqrt(n)+1)):
        for b in range(int(math.sqrt(n)+1)):
            if((a**2 + b**2 == n) and (a<=b)):
                print("(",a,",",b,")", sep = '', end = ' ')
    t-=1
    print('\n',end = '')