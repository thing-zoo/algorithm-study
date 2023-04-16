from itertools import combinations
n = int(input())

power = []
for _ in range(n):
    power.append(list(map(int, input().split())))

members = [i for i in range(n)]
start = 0
link = 0
minGap = 999999999999

for team1 in combinations(members, n//2): # team1 꾸리기
    start = 0
    link = 0
    team2 = []
    for t in range(n):
        if t not in team1:
            team2.append(t)
    for i in team1:
        for j in team1:
            start += power[i][j]
    for i in team2:
        for j in team2:
            link += power[i][j]
    minGap = min(minGap, abs(start-link))
print(minGap)