n, c = map(int, input().split())
data = input().split()
d = {}
for x in data:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
arr = sorted(d.items(), key=lambda x: x[1], reverse=True)
for e in arr:
    for _ in range(e[1]):
        print(e[0], end=" ")