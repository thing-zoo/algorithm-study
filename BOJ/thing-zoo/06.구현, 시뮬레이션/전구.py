n, m = map(int, input().split())
s = list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        s[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if s[i]: s[i] = 0
            else: s[i] = 1
    elif a == 3:
        for i in range(b-1, c):
            s[i] = 0
    else:
        for i in range(b-1, c):
            s[i] = 1
print(' '.join(map(str, s)))