n = int(input())
cow = [-1]*11
answer = 0
for _ in range(n):
    num, pos = map(int, input().split())
    if cow[num] == -1:
        cow[num] = pos
    elif cow[num] != pos:
        cow[num] = pos
        answer += 1
print(answer)