n, m = map(int, input().split())
a = list(map(int, input().split()))

answer = 0
end = 0
total = a[0]
for start in range(n):
    while end < n and total < m:
        end += 1
        if end != n: total += a[end]
    if end == n: break
    if total == m: answer += 1
    total -= a[start]
print(answer)