def solution(n, s, a, b, fares):
    answer = 0
    tree = [[float('inf')]*(n+1) for _ in range(n+1)]
    for f in fares:
        tree[f[0]][f[1]] = f[2]
        tree[f[1]][f[0]] = f[2]
    
    # 각 지점에서 어떤 지점까지의 최단 경로를 저장
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    tree[i][j] = 0
                else:
                    if tree[i][j] > tree[i][k] + tree[k][j]:
                        tree[i][j] = tree[i][k] + tree[k][j]
    # 어느 지점까지 같이 타고 가야 가장 적은 요금인지
    answer = tree[s][a] + tree[s][b]
    for i in range(1, n+1): # i 지점까지 같이 타고 간 후 i에서 각자 a, b로 이동하는 요금
        if answer > tree[s][i]+tree[i][a] +tree[i][b]:
            answer = tree[s][i]+tree[i][a] +tree[i][b]

    return answer