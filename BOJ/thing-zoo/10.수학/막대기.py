x = int(input())
n = 64
answer = 0
while x > 0:
    if x >= n:
        x -= n
        answer += 1
    n //= 2
print(answer)