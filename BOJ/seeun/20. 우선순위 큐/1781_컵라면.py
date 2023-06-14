import sys, heapq
input = sys.stdin.readline
n = int(input())
data = []
hq = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

# 데드라인, 컵라면개수 순서로 정렬
data.sort()
for i in range(n):
    deadline, noodle = data[i]
    heapq.heappush(hq, noodle) # 일단 힙에 현재 과제의 컵라면 개수 푸시

    # 만약 현재 과제를 데드라인안에 수행하지 못한다면
    if deadline < len(hq): # 지금까지 수행한 과제 중에 컵라면을 가장 적게주는 과제를 안함
        heapq.heappop(hq) # 가장 작은 컵라면 개수 빼내기
print(sum(hq))