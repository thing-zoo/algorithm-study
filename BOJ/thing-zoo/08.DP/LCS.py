# 계산 편의를 위해 맨 앞에 빈칸 삽입
a = ' ' + input()
b = ' ' + input()
# dp[i][j] = a[i], b[j]까지의 LCS 길이
dp = [[0]*len(b) for _ in range(len(a))]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]: # 같으면
            dp[i][j] = dp[i-1][j-1] + 1 # 이전까지의 값 + 1
        else: # 다르면
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 두가지 경우 비교
print(dp[-1][-1])