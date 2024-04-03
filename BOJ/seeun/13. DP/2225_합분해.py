n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0] = [1] * k # 0을 k개 가지고 0을 만드는 방법은 모두 1

for i in range(1, n+1): # i가 되는 수
    dp[i][1] = 1 # 숫자 하나로 i를 만드는 방법은 항상 1개
    
    for j in range(2, k+1): # j개를 합쳐서
        for p in range(i+1):
            dp[i][j] += dp[i-p][j-1] # j-1개의 숫자로 i-ㅔ를 만드는 개수를 모두 합침
        dp[i][j] %=  1000000000

print(dp[n][k])