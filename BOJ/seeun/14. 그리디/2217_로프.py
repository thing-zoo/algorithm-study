n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()
res = 0
for i in range(n):
    res = max(res, rope[i]*(n-i))
print(res)