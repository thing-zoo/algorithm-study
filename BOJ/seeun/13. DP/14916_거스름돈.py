# ========== DP===========
n = int(input())
if n <= 5:
    if n == 2 or n == 5:
        print(1)
    elif n == 4:
        print(2)
    else:
        print(-1)
else:
    dp = [float('inf')] * (n+1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n+1):
        dp[i] = min([dp[i], dp[i-2] + 1 , dp[i-5] + 1])
    print(dp[n])

# ========== 그리디===========
n = int(input())
cnt = 0
while True:
    if n % 5 == 0: # 5의 배수 || 2원으로 빼다가 0이 된 경우에도 여기서 걸림
        cnt += n//5 # 5원 짜리 동전 개수
        break
    else:
        n -= 2
        cnt += 1 # 2원 1개

    if n < 0:
        break
print(cnt if n >= 0 else -1)