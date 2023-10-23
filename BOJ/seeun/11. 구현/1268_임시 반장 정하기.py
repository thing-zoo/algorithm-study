n = int(input())
stud = [list(map(int, input().split())) for _ in range(n)]
maxnum = 0
maxstud = 0
for k in range(n): # k번 학생이 5년동안 같은반이었던 학생 카운트
    same = [False] * n # 같은 반이었던 적 있으면 True
    for j in range(5): # 학년 이동
        for i in range(n): # 학생 이동
            if stud[k][j] == stud[i][j]: # j학년일 때 i, k의 반이 같았으면
                same[i] = True
    
    # k와 같은반이었던 적이었던 학생 수
    cnt = same.count(True)
    if maxnum < cnt:
        maxnum = cnt
        maxstud = k+1

print(maxstud)
