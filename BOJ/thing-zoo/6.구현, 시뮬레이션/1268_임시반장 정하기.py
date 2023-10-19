n = int(input())
result = [set() for _ in range(n)] # 학생별 같은반이었던 학생집합
students = [[list() for _ in range(10)] for _ in range(5)] # 학년/반별 학생들
data = []
for i in range(n): # 학생
    data.append(list(map(int, input().split())))
    for j in range(5): # 학년
        students[j][data[i][j]].append(i)

for i in range(n): # 학생
    for j in range(5): # 학년
        for k in students[j][data[i][j]]:
            result[i].add(k)

answer = sorted(zip(result, [i+1 for i in range(n)]), key=lambda x: (-len(x[0]), x[1]))
print(answer[0][1])