n, k = map(int, input().split())
answer = 1
for i in range(1, n+1): answer *= i
for i in range(1, k+1): answer //= i
for i in range(1, n-k+1): answer //= i
print(answer)