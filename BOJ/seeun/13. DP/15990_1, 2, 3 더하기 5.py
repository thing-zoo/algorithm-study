t = int(input())
nums = [int(input()) for _ in range(t)]
maxi = max(nums)

# 1, 2, 3으로 끝나는 경우
dp = [[0 for _ in range(3)] for _ in range(maxi+1)]
dp[1] = [1, 0, 0] # 1
dp[2] = [0, 1, 0] # 2
dp[3] = [1, 1, 1] # 21, 12, 3
for i in range(4, maxi+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009 # i-1 수에 1을 붙일 수 있는 경우만 더하기
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009 # i-2 뒤에 2를 붙이기
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009 # i-3 뒤에 3 붙이기

for n in nums:
    print(sum(dp[n]) % 1000000009)