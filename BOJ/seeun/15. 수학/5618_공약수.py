# 반복문
n = int(input())
nums = list(map(int, input().split()))

for i in range(1, min(nums)+1):
    flag = True
    for num in nums:
        if num % i != 0: # 나누어 떨어지지 않는 수가 있으면 공약수 아님
            flag = False
            break
    if flag: # 모든 수가 나누어 떨어질 때만 출력
        print(i)

# gcd 함수
from math import gcd
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

# 최대공약수 구하기
if n == 2:
    gcdnum = gcd(nums[0], nums[1])
else:
    gcdnum = gcd(nums[0], gcd(nums[1], nums[2]))

for i in range(1, gcdnum//2+1):
    flag = True
    if gcdnum % i == 0:
        print(i)
print(gcdnum)