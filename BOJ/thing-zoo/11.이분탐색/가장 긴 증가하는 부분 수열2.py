# LIS O(nlogn) 로직
from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
x = [0] # x[i] = 길이가 i인 LIS중 최소값 저장
for i in range(n):
    j = bisect_left(x, a[i])
    if j == len(x):
        x.append(a[i])
    elif x[j] > a[i]:
        x[j] = a[i]
print(len(x)-1)