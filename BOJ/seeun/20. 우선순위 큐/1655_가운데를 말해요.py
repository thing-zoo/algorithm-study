import sys, heapq
input = sys.stdin.readline
n = int(input())
lq = []
rq = []

# 첫번째값
mid = int(input())
print(mid)

# 두번째 ~ 마지막 숫자
for i in range(n-1): 
    x = int(input())
    if x<mid: # 중간값보다 작으면 왼쪽 힙에 저장
        heapq.heappush(lq, -x)
    else:
        heapq.heappush(rq, x)

    # 중간값 갱신
    if i%2: # 홀수개 숫자를 불렀다면
        if len(lq)+2 == len(rq): # 방금 숫자가 오른쪽에 들어왔으면 -> 짝수개일때는 항상 왼쪽힙이 하나 적게 가지고 있음
            heapq.heappush(lq, -mid) # 중간값을 왼쪽에 넣고
            mid = heapq.heappop(rq) # 오른쪽에서 가장 작은 값이 중간 값
    else: # 짝수개의 숫자를 불렀다면 
        if len(lq)>len(rq): # 방금 숫자가 왼쪽에 들어왔으면 -> 짝수일때는 더 작은 값을 선택해야하기 때문에 둘중 왼쪽 값으로 설정
            heapq.heappush(rq, mid)
            mid = -heapq.heappop(lq)
    print(mid)