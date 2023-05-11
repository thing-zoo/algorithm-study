a, b, c = map(int, input().split())

e, m, s = 0, 0, 0
cnt = 0
while a!=e or b!=s or c != m:
    cnt += 1
    e += 1
    s+= 1
    m += 1
    if e> 15:
        e = 1
    if s > 28:
        s = 1
    if m >19:
        m = 1

print(cnt)