import heapq
t = int(input())

for _ in range(t):
    minh = []
    maxh = []
    n = int(input())
    visited = [False] * n
    for i in range(n):
        op, num = input().split()
        num = int(num)
        if op == "I": # 삽입 연산
            heapq.heappush(minh, (num, i))
            heapq.heappush(maxh, (-num, i))
            visited[i] = True # 아이디가 i인 숫자가 들어있음
        else:
            if num == 1: # 최댓값 삭제
                while maxh and not visited[maxh[0][1]]: # 최댓값의 아이디가 false이면 없는 숫자(최솟값 삭제에서 삭제되었을 수도)니까 없애기
                    heapq.heappop(maxh) # 허수 삭제
                if maxh: # 큐가 비어있지 않으면
                    # 진짜 최댓값 삭제
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)
            else: # 최솟값 삭제
                while minh and not visited[minh[0][1]]: # 허수인 최솟값을 다 삭제하기(최댓값 삭제에서 지워졌을 수도 있는 값)
                    heapq.heappop(minh) # 허수 삭제
                if minh: # 큐가 비어있지 않으면
                    # 진짜 최솟값 삭제
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)
    if True not in visited: # 아무 숫자도 남아있지 않으면
        print("EMPTY")
    else:
        # 정수가 있다면
        # 연산이 끝난 후 제거 되지 못한 최대 힙과 최소 힙을 팝하여 제거
        while maxh and visited[maxh[0][1]] == False:
            heapq.heappop(maxh)
        while minh and visited[minh[0][1]] == False:
            heapq.heappop(minh)

        # 최대 힙, 최소 힙 출력
        print(-maxh[0][0], minh[0][0])