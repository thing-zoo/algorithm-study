name = input()
n = int(input())
team = [input() for _ in range(n)]
team.sort()
ans = -1
teamname = ""
for t in team:
    L, O, V, E = name.count("L"), name.count("O"), name.count("V"), name.count("E") # 연두의 이름에 있는 LOVE 개수
    
    # 팀 이름에 있는 LOVE 개수 더하기
    L += t.count("L")
    O += t.count("O")
    V += t.count("V")
    E += t.count("E")

    # 공식에 따라 계산
    tmp = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if ans < tmp:
        ans = tmp
        teamname = t

print(teamname)