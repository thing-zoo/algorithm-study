n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

# 이진탐색
def bin(num, arr):
    s = 0
    e = len(arr)-1
    while s<=e:
        m = (s+e)//2
        if arr[m] == num:
            return m
        elif arr[m] < num:
            s = m+1
        else:
            e = m-1
    return -1

flag = False # 차집합에 포함되는 것이 있는지
cnt = 0
ans = []
for i in range(n):
    if bin(a[i], b) == -1: # a인데 b에는 포함되지 않으면
        flag = True 
        cnt += 1
        ans.append(a[i]) # 차집합 배열에 추가

if not flag: # 차집합이 하나도 없었으면
    print(0)
else: # 차집합이 있으면
    print(cnt)
    ans.sort()
    print(*ans)