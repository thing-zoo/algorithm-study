import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
d_name = {}
d_no = {}
for i in range(1, n+1):
    name = input().strip()
    d_name[name] = i
    d_no[i] = name
for _ in range(m):
    info = input().strip()
    if info.isdigit():
        print(d_no[int(info)])
    else:
        print(d_name[info])