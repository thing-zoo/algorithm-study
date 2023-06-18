import heapq, sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    heapq.heapify(nums)
    res = 0
    while len(nums) > 1: # 파일이 하나가 될 때 까지 진행
        a, b = heapq.heappop(nums), heapq.heappop(nums) # 가장 작은 두개의 파일 꺼내옴
        res += a+b # 두개를 합치는데 필요한 비용 누적하기
        heapq.heappush(nums, a+b) # 합친 파일을 다시 힙에 넣음
    print(res) # 현재까지 든 비용 출력