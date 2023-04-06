def check(i): # i행 점검
    for t in range(i): # 이전 행들 중에 같은 열에 있거나 대각선에 있으면 False(i행 지금 상태는 조건만족X)
        if queens[i] == queens[t] or (abs(i-t) == abs(queens[i]-queens[t])):
            return False
    return True

def dfs(i): # 행
    global cnt   
    
    if i == n: # 퀸 다 놓았으면
        cnt += 1
    else:
        for q in range(n): # 열 검사
            queens[i] = q # 일단 i, q에 퀸 놓음
            if check(i): # 그 행이 조건을 만족하는지 체크
                dfs(i+1) # 지금 상태가 조건을 만족하면 다음 행으로 넘어감

n = int(input())
cnt = 0
queens = [0] * n
dfs(0)
print(cnt)