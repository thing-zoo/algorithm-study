n, k = map(int, input().split())
wv = [[0, 0]]
wv.extend([list(map(int, input().split())) for _ in range(n)])
bag = [[0]*(k+1) for _ in range(n+1)]

maxvalue = 0
for i in range(1, n+1): # i번째 물건을 담을 수 있을 때
    for j in range(1, k+1): # j무게를 담을 수 있을 때
        if wv[i][0] <= j:
            # 이전 물건까지의 최댓값 vs 현재 물건 + 이전 물건
            bag[i][j] = max(bag[i-1][j], wv[i][1]+bag[i-1][j-wv[i][0]])
        else: # 무게 넘으면 못담으니까 그냥 이전 물건까지의 최댓값을 복사
            bag[i][j] = bag[i-1][j]
    tmp = max(bag[i])
    maxvalue = max(maxvalue, tmp)
print(maxvalue)
