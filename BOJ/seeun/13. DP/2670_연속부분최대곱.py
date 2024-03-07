import sys
input = sys.stdin.readline
n = int(input())
nums = [float(input()) for _ in range(n)]

for i in range(1, n):
    nums[i] = max(nums[i-1] * nums[i], nums[i])

print('%.3f' %max(nums))