import heapq
def solution(hq, K):
    answer = 0
    heapq.heapify(hq)
    if sum(hq) == 0 and K > 0: # 모두 0이면
        return -1 # 불가능
    while hq[0] < K: # 모든 값이 K이상일때까지
        if len(hq) < 2: # 두 요소가 없으면
            return -1   # 불가능
        a = heapq.heappop(hq) 
        b = heapq.heappop(hq)
        a = a + b*2
        heapq.heappush(hq, a)
        answer += 1
    return answer
def solution2(scoville, K): 
    # 다른분 코드 
    # 따로 모두 0인 경우 예외 처리없으니 깔끔해보여요
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
scoville = [0,0,1]
K = 10
print(solution(scoville, K))