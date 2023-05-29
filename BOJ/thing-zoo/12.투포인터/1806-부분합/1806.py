n, s = map(int, input().split())
a = list(map(int, input().split()))

answer = 1e5
end = 0
total = a[0]
for start in range(n):
    while end < n and total < s:
        end += 1
        if end < n: total += a[end]
    if end == n: break
    answer = min(answer, end - start + 1)
    total -= a[start]
print(answer if answer != 1e5 else 0)