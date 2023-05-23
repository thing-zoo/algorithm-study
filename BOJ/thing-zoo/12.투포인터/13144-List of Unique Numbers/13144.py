n = int(input())
a = list(map(int, input().split()))

answer = 0
count = {}
end = 0
for start in range(n):
    while end < n and a[end] not in count:
        count[a[end]] = 1
        end += 1
    answer += end - start
    count.pop(a[start])
print(answer)