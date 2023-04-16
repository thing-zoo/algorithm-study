from itertools import combinations
def solution():
    gap = 198 # 최대 차이값
    for start in combinations(range(n), n//2): # 절반 고르는 조합
        start_stats = 0
        link_stats = 0
        link = []
        for i in range(n):
            if i not in start:
                link.append(i) # 나머지 넣어주기
        for i, j in combinations(start, 2): # 팀에서 2명 고르는 조합
            start_stats += s[i][j] + s[j][i] # 능력치 더해주기
        for i, j in combinations(link, 2):
            link_stats += s[i][j] + s[j][i]
        gap = min(gap, abs(start_stats-link_stats)) # 현재 차이보다 작으면 담기
    print(gap)

n = int(input())
s = [ list(map(int, input().split())) for _ in range(n) ]
solution()