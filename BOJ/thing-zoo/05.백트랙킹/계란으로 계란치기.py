def f(i, eggs):
    global answer
    if i == n: # 모든 계란을 방문했다면
        count = 0 # 깨진 계란 세기
        for e in eggs: 
            if e[0] <= 0:
                count += 1
        if answer < count: answer = count
        return # 종료
    if eggs[i][0] <= 0: # 손에 든 계란이 깨졌으면
        f(i+1, eggs) # 다음 계란으로
    else:
        flag = False
        for j in range(n):
            if i == j or eggs[j][0] <= 0: # 손에 든 계란이거나 깨진 계란이면
                continue # 넘어가기
            flag = True
            # 계란 치기
            eggs[i][0] -= eggs[j][1]
            eggs[j][0] -= eggs[i][1]
            f(i+1, eggs) # 다음 계란
            eggs[i][0] += eggs[j][1] # 이전 계란으로 복귀
            eggs[j][0] += eggs[i][1]
        if not flag: # 전부 깨진 계란이면
            f(n, eggs)
n = int(input())
eggs = [] # [내구도(s), 무게(w)]
for _ in range(n):
    eggs.append(list(map(int, input().split())))
answer = 0 # 깨진 계란의 최댓값
f(0, eggs)
print(answer)