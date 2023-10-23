import sys
input = sys.stdin.readline

n = int(input())
nums = [0]
nums += [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1:
    print(nums[1])
elif n == 2:
    print(nums[1] + nums[2])
else:
    dp[1] = nums[1]
    dp[2] = nums[1] + nums[2]
    for i in range(3, n+1):
        # ex) dp[3]: 1+3, 2+3, "1+2"도 고려해야함. 자신을 안 먹는 것도 경우에 포함
        dp[i] = max([dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i], dp[i-1]]) 
    print(max(dp))