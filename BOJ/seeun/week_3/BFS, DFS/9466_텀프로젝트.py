import sys

sys.setrecursionlimit(200000) # 크기 안 늘려주면 채점할때 오류남
input = sys.stdin.readline

stack = []
visited = []
cnt = 0
def dfs(me, mypick):
    global stack, stud_num, visited, cnt
    stack.append(me)
    visited[me] = 1

    if visited[mypick] == 1: # 이미 팀 짜는데 들어가잇으면
        if mypick in stack:
            cnt += len(stack[stack.index(mypick):]) # 팀 완성 된 만큼만 자르기
            return
    else:
        dfs(mypick, stud[mypick])

n = int(input())

stud_num = 0
for _ in range(n):
    res = []
    stud = []
    stud_num = int(input())
    visited = [0] * (stud_num+1)

    stud = [0]
    stud.extend(list(map(int, input().split())))

    cnt = 0
    for i in range(1, stud_num+1):
       if visited[i] == 0: # 방문 안한거면 팀원 만들러 가기
            stack = []
            dfs(i, stud[i])
    print(stud_num-cnt)
