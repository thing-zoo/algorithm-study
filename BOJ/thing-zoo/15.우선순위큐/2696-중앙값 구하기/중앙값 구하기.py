import heapq
t = int(input())
for _ in range(t):
    m = int(input())
    data = []
    for i in range(0, m+1, 10):
        data += list(map(int, input().split()))
    
    left = []  # n/2+1, 최대힙
    right = [] # n/2, 최소힙
    answer = []
    for i in range(m):
        if not left or -left[0] > data[i]:
            heapq.heappush(left, -data[i])
        elif not right or right[0] < data[i]:
            heapq.heappush(right, data[i])
        else:
            heapq.heappush(left, -data[i])
        
        while len(left) > ((i+1)//2+1):
            heapq.heappush(right, -heapq.heappop(left))
        while len(right) > (i+1)//2:
            heapq.heappush(left, -heapq.heappop(right))
        
        if i%2 == 0:
            answer.append(-left[0])
    print(len(answer))
    for i in range(0, len(answer), 10):
        print(' '.join(map(str, answer[i:i+10])))
    