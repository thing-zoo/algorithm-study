import heapq, sys
input = sys.stdin.readline
n = int(input())
maxh = []
minh = []
prob = {}
for _ in range(n):
    p, l = map(int, input().rstrip().split())
    heapq.heappush(maxh, (-l, -p))
    heapq.heappush(minh, (l, p))
    prob[p] = True

m = int(input())
for _ in range(m):
    comm = list(input().rstrip().split())
    if comm[0] == "recommend":
        if comm[1] == "1":
            while maxh and not prob[-maxh[0][1]]: # 이미 삭제된 문제들을 힙에서 제거
                heapq.heappop(maxh)
            if maxh: # 문제가 남아있으면 문제 번호 * -1 출력
                print(-maxh[0][1])
        else:
            while minh and not prob[minh[0][1]]:
                heapq.heappop(minh)
            if minh:
                print(minh[0][1])
        
    elif comm[0] == "add":
        # 이미 삭제된 문제들을 힙에서 제거함
        while maxh and not prob[-maxh[0][1]]: 
            heapq.heappop(maxh)
        while minh and not prob[minh[0][1]]:
            heapq.heappop(minh)
        p, l = int(comm[1]), int(comm[2])
        heapq.heappush(maxh, (-l, -p))
        heapq.heappush(minh, (l, p))
        prob[p] = True # 문제 있음

    else:
        p = int(comm[1]) 
        prob[p] = False # p문제 없어짐