import math
n = int(input())
nums = list(map(int, input().split()))

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(num)+1)):
            print(i)
            if num % i == 0:
                return False
        return True

cnt = 0
for i in range(n):
    if isPrime(nums[i]):
        cnt += 1

print(cnt)