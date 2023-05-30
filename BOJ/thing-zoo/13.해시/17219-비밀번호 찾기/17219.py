n, m = map(int, input().split())
d = {}
for _ in range(n):
    site, pw = input().split()
    d[site] = pw
for _ in range(m):
    site = input()
    print(d[site])