def f(x):
    global answer
    if x == n: # 퀸을 다 놓았다면
        answer += 1
        return # 탈출
    for y in range(n):
        if column[y] or diagonal_l[x+y] or diagonal_r[x-y+n-1]: # 같은 열이거나 대각선상이면
            continue # 건너뛰기
        column[y] = True
        diagonal_l[x+y] = True
        diagonal_r[x-y+n-1] = True
        f(x+1) # 다음 퀸으로
        column[y] = False
        diagonal_l[x+y] = False
        diagonal_r[x-y+n-1] = False

n = int(input())
answer = 0  # 퀸을 놓는 방법의 수
queens = [] # 퀸의 위치
column = [False]*n # 해당열의 막힘 여부
diagonal_l = [False]*(2*n-1) # 왼쪽 대각선의 막힘 여부
diagonal_r = [False]*(2*n-1) # 오른쪽 대각선의 막힘 여부
f(0)
print(answer)