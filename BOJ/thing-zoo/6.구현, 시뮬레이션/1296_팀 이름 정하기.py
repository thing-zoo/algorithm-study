love = "LOVE"
green = input()
count = [green.count(love[i]) for i in range(4)]
result = []
for _ in range(int(input())):
    team = input()
    count2 = [count[i] + team.count(love[i]) for i in range(4)]
    score = 1
    for i in range(4):
        temp = []
        for j in range(i+1, 4):
            temp.append(count2[i]+count2[j])
        for j in temp:
            score *= j
    result.append((score%100, team))
result.sort(key=lambda x: (-x[0], x[1]))
print(result[0][1])