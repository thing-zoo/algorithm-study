import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    # 한줄에 10개씩 있기 때문에 여러번 입력 받아야함
    for _ in range(n//10):
        nums.extend(list(map(int, input().split())))
    nums.extend(list(map(int, input().split())))

    res = [] # 케이스 별로 정답 저장할 배열
    hq = [] # 힙
    for i in range(1, n+1):
        heapq.heappush(hq, nums[i-1])
        if i % 2 == 1: # 홀수번째 숫자를 받으면
            tmp = []
            for _ in range(i//2): # i//2개를 임시로 pop하기
               tmp.append(heapq.heappop(hq))
            res.append(hq[0]) # 중앙값 저장
            for t in tmp: # pop한 숫자들 다시 push
                heapq.heappush(hq, t)
    print(len(res)) # 개수 출력
    for i in range(0, len(res), 10): # 한줄에 10개씩 출력
        print(*res[i:i+10])
