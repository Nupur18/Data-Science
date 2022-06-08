from math import sqrt
primes = [2]

for i in range(3,32000,2):
    isprime = True

    cap = sqrt(i)+1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break
    if (isprime):
        primes.append(i)

T = eval(input())
output = ""
for t in range(0,T):

    if (t > 0):
        output += "\n"

    M,N = input().split(' ')
    M = int(M)
    N = int(N)
    cap = sqrt(N)+1

    if (M < 2):
        M = 2

    isprime = [True]*100001

    for i in primes:
        if (i >= cap):
            break

        if (i >= M):
            start = i*2
        else:
            start = M + ((i - M % i)%i)
        falseblock = [False] * len(isprime[start-M:N+1-M:i]);
        isprime[start-M:N+1-M:i] = falseblock

    for i in range(M,N+1):
        if (isprime[i-M] == True):
            output += str(i) + " "

print(output[:-1])