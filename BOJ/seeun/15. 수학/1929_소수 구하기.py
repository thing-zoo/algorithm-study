import math
a, b = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True

cnt = 0
for i in range(a, b+1):
    if isPrime(i):
        print(i)
