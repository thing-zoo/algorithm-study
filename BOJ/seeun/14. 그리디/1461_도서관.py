n, m = map(int , input().split())
books = list(map(int, input().split()))
neg = []
pos = []
for b in books:
    if b < 0:
        neg.append(b)
    else:
        pos.append(b)

# 양수, 음수 따로 / 절댓값이 큰 순서대로
neg.sort() 
pos.sort(reverse = True)

ans = 0
stack = []
for i in range(0, n, m): # m개씩 묶어서 나름
    if i < len(neg):
        stack.append(abs(neg[i]))
    if i < len(pos):
        stack.append(pos[i])

stack.sort()
for i in range(len(stack)-1): # 0 <-> 제자리 왕복
    ans += stack[i]*2

# 마지막 묶음은 편도로 움직임
ans += stack[-1]
print(ans)