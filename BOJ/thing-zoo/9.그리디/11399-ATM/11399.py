n = int(input())
p = list(map(int, input().split()))
p.sort()
t = [p[0]]+[0]*n
for i in range(1, n):
    t[i] = t[i-1] + p[i]
print(sum(t))