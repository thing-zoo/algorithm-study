from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
end = 0
answer = 0
count = defaultdict(int)
for start in range(n):
    while end < n:
        if count[a[end]] == k: break
        count[a[end]] += 1
        end += 1
    answer = max(answer, end - start)
    if end == n: break
    count[a[start]] -= 1
    if count[a[start]] == 0: count.pop(a[start])
print(answer)