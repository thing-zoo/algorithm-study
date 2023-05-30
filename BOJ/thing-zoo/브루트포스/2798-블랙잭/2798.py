from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0 # 합의 최대값
for selected in combinations(cards, 3): # 3개 선택
    total = sum(selected) # 합구하기
    if total <= m: # m이하면
        answer = max(answer, total) # 정답갱신
        if total == m: # 최대값이므로
            break # 탈출
print(answer)