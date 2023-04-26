import sys
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().rstrip().split())))

d = [0]*(n+1)
for i in range(n):
    day, money = data[i]
    for j in range(i+day, n+1): # i번째 일을 끝 냈을 때, 끝낸 이후의 돈 갱신
        if d[j] < d[i] + money: # 원래 그날 벌 수 있는 돈 < i번째 날까지 벌어놓은돈 + i번째 일을 해서 벌 돈
            d[j] = d[i] + money
        # print(i, j, d)
print(d[n])