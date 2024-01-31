n = int(input())
radius = list(map(int, input().split()))
radius.sort()
answer = 1
for r in range(2, 101):
    count = 0
    for j in range(n):
        if radius[j]%r == 0:
            count += 1
    answer = max(answer, count)
print(answer)