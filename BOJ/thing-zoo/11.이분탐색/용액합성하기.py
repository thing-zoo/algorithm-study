# x + y = 0, y = -x
import bisect
n = int(input())
a = sorted(list(map(int, input().split())))

answer = 1e9
for i in range(n):
    j = bisect.bisect_left(a, -a[i])
    if j-1 != i and j-1 > 0 and abs(answer) > abs(a[i] + a[j-1]):
        answer = a[i] + a[j-1]
    if j != i and j < n and abs(answer) > abs(a[i] + a[j]):
        answer = a[i] + a[j]
    if j+1 != i and j+1 < n and abs(answer) > abs(a[i] + a[j+1]):
        answer = a[i] + a[j+1]
print(answer)