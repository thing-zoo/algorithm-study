import sys
input = sys.stdin.readline
n = int(input())
nums = [0] * 10001
for _ in range(n):
    tmp = int(input())
    nums[tmp] += 1

for  i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)