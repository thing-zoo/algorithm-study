n, score, p = map(int, input().split())
if n == 0: # 랭킹이 없으면
    rank = 1 # 1등
else: # 랭킹이 있으면
    scores = list(map(int, input().split()))

    if n == p and score <= scores[-1]: # 랭킹이 꽉찼고 점수가 크지않다면
        rank = -1 # 랭킹에 반영안됨
    else:
        rank = n + 1 # 맨마지막 랭킹으로 초기화
        for i in range(n):
            if scores[i] <= score: # 기존점수 이상이면
                rank = i + 1 # 그게 등수
                break
print(rank)