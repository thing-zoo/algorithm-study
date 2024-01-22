n, m = map(int, input().split())
s = [input() for _ in range(n)]
answer = 0
for _ in range(m):
    x = input()
    if x in s:
        answer += 1
print(answer)