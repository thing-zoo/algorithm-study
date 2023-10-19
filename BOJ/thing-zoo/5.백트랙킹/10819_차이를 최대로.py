def dfs(result, check):
    global answer
    if len(result) == n:
        total = 0
        for i in range(n-1):
            total += abs(result[i] - result[i+1])
        answer = max(answer, total)

    for i in range(n):
        if i not in check:
            dfs(result+[a[i]], check + [i])


n = int(input())
a = list(map(int, input().split()))
answer = 0
dfs([], [])
print(answer)