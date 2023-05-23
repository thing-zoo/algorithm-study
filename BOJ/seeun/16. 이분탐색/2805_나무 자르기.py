n, m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()
s = 1
e = tree[-1]
ans = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for t in tree:
        if t>mid:
            cnt += t-mid
    if cnt >= m:
        s = mid + 1
        ans = max(ans, mid)
    else:
        e = mid -1

print(ans)