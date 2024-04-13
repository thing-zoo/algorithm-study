import sys, heapq
input = sys.stdin.readline
n = int(input())
ans = 1
hq = []
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort() # 시작시간이 빠른 순서대로 정렬
heapq.heappush(hq, meeting[0][1])
for i in range(1, n):
    if hq[0] <= meeting[i][0]: # 현재 회의실 중 가장 빨리 끝나는 시간 <= 현재 회의 시작 시간
        heapq.heappop(hq) # 끝난 회의 삭제
    else: # 열린 회의실에서 현재 회의를 시작할 수 있지 않으면
        ans += 1 # 새로운 회의실 하나 더 열기
    heapq.heappush(hq, meeting[i][1]) # 현재 회의 삽입
print(ans)