from collections import defaultdict
n = int(input())
dp = [0] * (n+1)
if n < 2:
    print(0)
else:
    dp[2] = 3
    type = defaultdict(int)
    type[2] = 3
    for i in range(2, n+1):
        if 3*i % 2 != 0: # 넓이가 2의 배수가 아니면 패스
            continue
        if i >= 4 and i % 2 == 0: # 2의 배수가 될때마다 특별 모양 추가
            dp[i] += 2
            type[i] += 2
        for j in range(2,i, 2): # 
            dp[i] += dp[j] * type[i-j] # 너비j를 채우는 모든 모양 개수 * i-j에 해당하는 유일한 모양 개수
    # print(dp, type)
    print(dp[n])