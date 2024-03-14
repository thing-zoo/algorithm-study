n, k = map(int, input().split()) # 돌의 개수, 한번에 쓸 수 있는 최대힘
a = list(map(int, input().split())) # 각 돌에 부여되어 있는 수
dp = [False]*n # 위치별 도달 가능 여부
dp[0] = True # 시작점 초기화
for i in range(n-1): # 0~n-1번째 돌에 대해
    if not dp[i]: continue # 도달할 수없으면 넘기기
    for j in range(i+1, n): # 다음 돌 찾기
        if (j-i)*(1+abs(a[i]-a[j])) <= k: # 건너갈수 있으면
            dp[j] = True # 도달 가능 체크
print('YES' if dp[n-1] else 'NO') # 마지막돌에 도달하면 예스