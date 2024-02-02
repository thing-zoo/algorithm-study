# 최장 증가 부분 수열(LIS: Longest Increasing Subsequence)
# O(n^2)
n = int(input())
a = list(map(int, input().split()))
# dp[i]=a[i]를 마지막값으로 가지는 LIS의 길이
dp = [1]*n # 처음 길이는 1로 초기화
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]: # 증가하는 형태면
            dp[i] = max(dp[j] + 1, dp[i]) # 기존과 j까지의 LIS 길이 비교
print(max(dp)) # 그중에서 최대값 반환