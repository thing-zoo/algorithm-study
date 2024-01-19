# 개선된 코드
import heapq
t = int(input())
for _ in range(t):
    m = int(input())
    data = []
    for i in range(m//10 + 1):
        data += list(map(int, input().split()))
    
    left, mid, right = [], data[0], [] # 수열을 최대힙, 중앙값, 최소힙으로 나누어 표현
    answer = [data[0]]
    for i in range(1, m):
        if data[i] < mid:
            heapq.heappush(left, -data[i])
        else:
            heapq.heappush(right, data[i])
        
        if i%2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            answer.append(mid)
    print(len(answer))
    for i in range(len(answer)):
        if i%10 == 0: print()
        print(answer[i], end=' ')
    print()