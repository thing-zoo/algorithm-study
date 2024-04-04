import sys
input = sys.stdin.readline # 보통 입력이 10만 이상이면 입력에서 시간초과가 나는것 같음!

n, m = map(int, input().split()) # 영토의 크기
# dp[i][j] = (0,0)~(i,j) 직사각형 내 합
# 계산 편의상 0행, 0열 추가해준다
dp = [[0]*(m+1)]
for _ in range(n):
    dp.append([0]+list(map(int, input().rstrip().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] += dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])