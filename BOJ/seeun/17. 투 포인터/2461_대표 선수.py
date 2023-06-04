import heapq
n, k = map(int, input().split())
stud = [sorted(list(map(int, input().split()))) for _ in range(n)]

gap = 10**9+1
idx = [1]*n # 각 반마다 포인터
hq = [] # 작은값 순서대로 뽑아줄 힙
maxnum = 0
minnum = 10e9
minidx = -1

for i in range(n):
    maxnum = max(stud[i][0], maxnum) # 제일 작은 것들 중에 가장 큰거
    heapq.heappush(hq, (stud[i][0], i)) # 배열마다 제일 작은 값들 저장

while True:
    tmp = heapq.heappop(hq) # 가장 작은값과 그 값의 위치 받기
    minnum = tmp[0]
    minidx = tmp[1] # 몇반인지

    gap = min(gap, maxnum - minnum)
    if idx[minidx] == k:
        break
    heapq.heappush(hq, (stud[minidx][idx[minidx]], minidx)) # 현재 반의 최솟값은 넘기고 다음으로 작은 값 저장
    maxnum = max(maxnum, stud[minidx][idx[minidx]]) # 포인터가 넘어갔으니 최댓값도 갱신
    idx[minidx] += 1 # 포인터 증가시켜주기

print(gap)