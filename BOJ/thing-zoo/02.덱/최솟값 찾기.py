from collections import deque
n, l = map(int, input().split())
a = list(map(int, input().split()))
candi = deque()
for i in range(n):
    while candi and candi[-1][1] > a[i]: # 현재값보다 큰 후보
        candi.pop() # 삭제
    while candi and candi[0][0] < i - l + 1: # 현재구간이 아닌 후보
        candi.popleft() # 삭제
    candi.append([i, a[i]])
    print(candi[0][1], end=" ")