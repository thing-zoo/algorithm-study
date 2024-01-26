answer, tired = 0, 0
a, b, c, m = map(int, input().split())
for i in range(24):
    if tired + a <= m:
        answer += b
        tired += a
    else:
        tired -= c
        if tired < 0: 
            tired = 0
print(answer)