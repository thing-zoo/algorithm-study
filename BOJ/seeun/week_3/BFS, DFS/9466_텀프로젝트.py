import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

stack = []
visited = []
cnt = 0
def dfs(me, mypick):
    global stack, stud_num, visited, cnt
    stack.append(me)
    visited[me] = 1

    if visited[mypick] == 1:
        if mypick in stack:
            cnt += len(stack[stack.index(mypick):])
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
       if visited[i] == 0:
            stack = []
            dfs(i, stud[i])
    print(stud_num-cnt)
