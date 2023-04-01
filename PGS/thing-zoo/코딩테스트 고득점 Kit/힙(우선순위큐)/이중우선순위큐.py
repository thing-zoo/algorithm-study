import heapq
def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    for operation in operations:
        order, value = operation.split()
        if order == "I": # 삽입
            heapq.heappush(min_heap, int(value))
            heapq.heappush(max_heap, -int(value))
        else: #삭제
            if int(value) == 1: #최댓값 삭제
                if max_heap:
                    min_heap.remove(-max_heap[0])
                    heapq.heappop(max_heap)
            else: # 최솟값 삭제
                if max_heap:
                    max_heap.remove(-min_heap[0])
                    heapq.heappop(min_heap)
    if max_heap:
        answer = [-max_heap[0], min_heap[0]]
    else:
        answer = [0,0]
    return answer
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))