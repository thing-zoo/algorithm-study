import bisect
n = int(input())
solutions = list(map(int, input().split()))
dist = 2e9
answer = []
for i in range(n):
    j = bisect.bisect_left(solutions, -solutions[i]) # lower_bound는 삽입할 가장 왼쪽 인덱스로 같거나, 더 큰 수중 가장 작은수
    if i != j - 1 and j - 1 > 0 and dist > abs(solutions[i]+solutions[j-1]): # i랑 같지 않고 범위내, 0에 더 가까우면
        dist = abs(solutions[i]+solutions[j-1])
        answer = [solutions[i], solutions[j-1]]
    if i != j and j < n and dist > abs(solutions[i]+solutions[j]):
        dist = abs(solutions[i]+solutions[j])
        answer = [solutions[i], solutions[j]]
    if i != j + 1 and j + 1 < n and dist > abs(solutions[i]+solutions[j+1]):
        dist = abs(solutions[i]+solutions[j+1])
        answer = [solutions[i], solutions[j+1]]
print(*sorted(answer))