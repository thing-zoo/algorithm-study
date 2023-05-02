import sys, heapq
input = sys.stdin.readline

n = int(input())
times = []
lectures = []
for _ in range(n):
    times.append(list(map(int, input().rstrip().split())))

times.sort(key=lambda x:(x[0], x[1]))

ans = 0
heapq.heappush(lectures, times[0][1])
for i in range(1, n):
    if times[i][0] < lectures[0]: # 다음 강의의 시작시간이 가장 빨리 마치는 강의의 마치는 시간보다 이르면
        heapq.heappush(lectures, times[i][1]) # 다른 강의실을 이용
    else: # 가장 빨리 마치는 강의의 마치는 시간보다 늦으면
        heapq.heappop(lectures) # 그 강의실 이어서 사용 가능 -> 강의완료 처리(pop)
        heapq.heappush(lectures, times[i][1]) # 강의 추가
print(len(lectures))