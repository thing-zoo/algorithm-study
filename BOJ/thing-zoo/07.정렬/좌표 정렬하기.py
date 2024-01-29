n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
for e in sorted(data):
    print(e[0], e[1], sep=" ")