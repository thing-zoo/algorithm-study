import bisect

t = int(input())
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nsum = []
msum = []
# i~j 합을 저장하는 배열, 반복문
for i in range(n):
    s = nlist[i]
    nsum.append(s)
    for j in range(i+1, n):
        s += nlist[j]
        nsum.append(s)
for i in range(m):
    s = mlist[i]
    msum.append(s)
    for j in range(i+1, m):
        s += mlist[j]
        msum.append(s)

nsum.sort()
msum.sort()
cnt = 0

# msum에서 t-a[i]+~+a[j] 값을 찾기
for i in range(len(nsum)):
    l = bisect.bisect_left(msum, t-nsum[i])
    r = bisect.bisect_right(msum, t-nsum[i])

    cnt += (r-l)
print(cnt)