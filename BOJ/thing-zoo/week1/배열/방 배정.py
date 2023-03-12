data = [[] for _ in range(6)]
n, k = map(int, input().split())
for i in range(n):
    s, y = map(int, input().split())
    data[y-1].append(s)
room = 0
for v in data:
    w = v.count(0)
    m = v.count(1)
    if w:
        room += w//k
        if w%k:
            room += 1
    if m:
        room += m//k
        if m%k:
            room += 1
print(room)