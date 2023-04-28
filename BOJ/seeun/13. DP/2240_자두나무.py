t, w = map(int, input().split())
tree = []
tree.append(0)
for _ in range(t):
    tree.append(int(input()))

d = [[0]*(t+1) for _ in range(w+1)]

# 초기값 설정 - 안 움직이고 1번에서 계속 받아먹는 경우
for i in range(1, t+1):
    if tree[i] == 1: 
        d[0][i] = d[0][i-1]+1
    else:
        d[0][i] = d[0][i-1]

for i in range(1, t+1):
    for j in range(1, w+1):
        # 받아먹을 수 있으면
        if  j%2==0 and tree[i] == 1: # 1번 나무 밑에 있는데 1번 나무에서 떨어지면
            d[j][i] = max(d[j][i-1], d[j-1][i])+1 #1번에 가만히 있는 상태에서 받기, 2번에 있다가 1번으로 이동해서 받기 둘중에 큰거
        elif  j%2==1 and tree[i] == 2:
            d[j][i] = max(d[j][i-1], d[j-1][i])+1
        else: # 못받아먹는 상황이면
            d[j][i] = max(d[j][i-1], d[j-1][i-1]) #이전 시간것들중에 큰거  
res = -1
for i in range(w+1):
    res = max(res, d[i][-1])
print(res)