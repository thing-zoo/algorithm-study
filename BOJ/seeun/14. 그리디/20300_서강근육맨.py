import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
if N % 2 == 1: # 홀수인 경우 가장 큰 숫자 제외하고 최소+최대와 max 비교
    maxnum = nums[N-1]
    for i in range(N-1):
        maxnum = max(maxnum, nums[i] + nums[N-i-2])
else: # 짝수인 경우 최대+최대와 max 비교
    maxnum = 0
    for i in range(N):
        maxnum = max(maxnum, nums[i] + nums[N-i-1])

print(maxnum)