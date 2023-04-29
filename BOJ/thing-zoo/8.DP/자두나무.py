t, w = map(int, input().split())
dp = [[0]*(w+1) for _ in range(t+1)]
for i in range(1, t+1):
    tree = int(input())
    for j in range(w+1):
        if tree == 1 and j == 0: # 현재위치에 자두가 떨어진 경우(한번도 안움직임)
            dp[i][j] = dp[i-1][j] + 1
        elif (tree == 1 and j%2 == 0) or (tree == 2 and j%2 != 0): # 현재위치에 자두가 떨어진 경우(움직인 경우)
            # j-1번 움직인 상태에서 1번 움직인 경우와 j번 움직인 상태에서 가만히 있는 경우
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j] + 1)
        else: # 현재위치에 자두가 안떨어진 경우
            dp[i][j] = dp[i-1][j]
print(max(dp[t]))