import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
dict = {}
for _ in range(n):
    k, v = input().rstrip().split()
    dict[k] = v

for _ in range(m):
    print(dict[input().rstrip()])