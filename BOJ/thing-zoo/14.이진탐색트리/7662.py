import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    max_heap, min_heap = [], []
    visited = [False]*k  # 삽입된 값 확인용
    for i in range(k):
        op, n = input().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
            visited[i] = True  # 삽입된 값 체크
        elif n == 1:
            # min_heap에서 삭제했던 값이면
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)  # 삭제하기
            if max_heap:
                visited[max_heap[0][1]] = False  # 삭제할 것이므로 거짓
                heapq.heappop(max_heap)
        else:
            # max_heap에서 삭제했던 값이면
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)  # 삭제하기
            if min_heap:
                visited[min_heap[0][1]] = False  # 삭제할 것이므로 거짓
                heapq.heappop(min_heap)
    # 삭제해야할 값이 남아있을 수 있으므로
    while max_heap and not visited[max_heap[0][1]]:  # min_heap에서 삭제했던 값이면
        heapq.heappop(max_heap)  # 삭제하기
    while min_heap and not visited[min_heap[0][1]]:  # max_heap에서 삭제했던 값이면
        heapq.heappop(min_heap)  # 삭제하기

    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")