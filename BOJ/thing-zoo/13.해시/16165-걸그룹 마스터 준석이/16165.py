n, m = map(int, input().split())
d_team = {}
d_member = {}
for _ in range(n):
    team = input()
    members = []
    for _ in range(int(input())):
        member = input()
        members.append(member)
        d_member[member] = team
    d_team[team] = members
for _ in range(m):
    quiz = input()
    type = input()
    if type == '1': print(d_member[quiz])
    else: print("\n".join(sorted(d_team[quiz])))