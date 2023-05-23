k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

line.sort()
s = 1
e = line[-1]
ans = 0
while s<=e:
    m = (s+e)//2
    cnt = 0
    for i in range(k):
        cnt += line[i]//m

    if cnt>=n:
        s = m+1
        ans = max(ans, m)
    else:
        e = m-1
print(ans)