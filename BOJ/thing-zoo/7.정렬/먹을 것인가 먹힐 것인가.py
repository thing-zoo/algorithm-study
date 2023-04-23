import sys
input = sys.stdin.readline
def count(k):
    start = 0
    end = n - 1
    total = 0
    while start <= end:
        mid = (start+end)//2
        if a[mid] > k:
            total = n - mid
            end = mid - 1
        else:
            start = mid + 1
    return total

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().strip().split())))
    b = sorted(list(map(int, input().strip().split())))
    answer = 0
    for i in b:
        answer += count(i)
    print(answer)