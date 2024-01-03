import sys
input = sys.stdin.readline
def solution():
    start = 1
    end = request[-1]
    while start <= end:
        mid = (start + end)//2
        total = 0
        for r in request:
            if r < mid:
                total += r
            else:
                total += mid
        if total <= budget:
            start = mid + 1
        else:
            end = mid - 1
    print(end)

n = int(input())
request = sorted(list(map(int, input().rstrip().split())))
budget = int(input())
solution()