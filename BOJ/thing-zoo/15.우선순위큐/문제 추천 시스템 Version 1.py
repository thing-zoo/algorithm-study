import heapq, sys
input = sys.stdin.readline
n = int(input())
easy, hard = [], []
levels = [0]*100001 # 0: 리스트에 없음, 1이상: 리스트에 존재 & 난이도
for _ in range(n):
    p, l = map(int, input().rstrip().split())
    heapq.heappush(hard, (-l, -p))
    heapq.heappush(easy, (l, p))
    levels[p] = l

m = int(input())
for _ in range(m):
    commands = input().rstrip().split()
    if commands[0] == 'recommend':
        if commands[1] == '1':
            while levels[-hard[0][1]] != -hard[0][0]: # 난이도가 다르면 리스트에 없는 것이므로
                heapq.heappop(hard) # 삭제
            print(-hard[0][1])
        else:
            while levels[easy[0][1]] != easy[0][0]:
                heapq.heappop(easy)
            print(easy[0][1])
    elif commands[0] == 'add':
        p, l = map(int, commands[1:])
        heapq.heappush(hard, (-l, -p))
        heapq.heappush(easy, (l, p))
        levels[p] = l
    elif commands[0] == 'solved':
        p = int(commands[1])
        levels[p] = 0 # 리스트에서 삭제