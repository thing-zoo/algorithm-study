import sys
input = sys.stdin.readline
d = {}
n = int(input())
for _ in range(n):
    x = int(input())
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
max_value = max(d.values())
arr = sorted(filter(lambda x: x[1] == max_value, d.items()))
print(arr[0][0])
