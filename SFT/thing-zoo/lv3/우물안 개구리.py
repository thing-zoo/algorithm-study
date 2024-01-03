n, m = map(int, input().split())
w = list(map(int, input().split()))
friends = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    friends[a-1] = max(friends[a-1], w[b-1]) 
    friends[b-1] = max(friends[b-1], w[a-1])

answer = 0
for i in range(n):
    if w[i] > friends[i]:
        answer += 1
print(answer)