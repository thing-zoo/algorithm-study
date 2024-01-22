n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
for e in sorted(data, key=lambda x: (x[1], x[0])):
    print(e[0], e[1], sep=" ")