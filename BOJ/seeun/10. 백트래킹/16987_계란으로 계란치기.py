n = int(input())

egg = []
broken = [False] * n

for i in range(n):
    egg.append(list(map(int, input().split())))

res = 0

def break_egg(i, egg):
    global res
    if i == n:
        answer = 0
        for eg in egg:
            if eg[0]<=0:
                answer += 1

        res = max(answer, res)
        return res

    if egg[i][0] <= 0: # 손에 든게 깨져있으면
        break_egg(i+1, egg) # 다음 계란 들기
    else:
        all_broken = True # 다 깨졌나?
        for e in range(len(egg)):
            if egg[e][0] >0 and i != e: # 깰 계란이 있으면
                all_broken = False # 아니 안깨진거 있음!
                egg[i][0] -= egg[e][1]
                egg[e][0] -= egg[i][1]
                break_egg(i+1, egg) # 내려놓고 다음 계란 듦
                egg[i][0] += egg[e][1]
                egg[e][0] += egg[i][1] 
        if all_broken: # 다깨졌으면
            break_egg(n, egg) # 마지막 결과 구하러 감
         
break_egg(0, egg)
print(res)