import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if scoville[0] < K and len(scoville)==1:
            return -1
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
    return answer

scoville, K = [1, 2, 3, 9, 10, 12],	7
print(solution(scoville, K))