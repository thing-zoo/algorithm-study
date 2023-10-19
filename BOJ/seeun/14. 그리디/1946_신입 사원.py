import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    score = [list(map(int, input().rstrip().split())) for _ in range(n)]
    score.sort() # [0] 순위 대로 정렬
    ans = 0
    stack = [score[0][1]]
    for i in range(1, n):
        if stack[-1] > score[i][1]: # [1]이 앞사람보다 높은 경우에만 스택에 들어감
            stack.append(score[i][1])
    print(len(stack))