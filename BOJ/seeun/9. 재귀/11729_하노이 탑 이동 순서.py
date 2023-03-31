def move(n, start, to):
    # print(start, to)
    res.append([start, to])

cnt = 0
res = []
def hanoi(n, start, to, via):
    global cnt
    cnt += 1
    if n == 1:
        move(n, start, to)
        
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1, via, to, start)

n = int(input())
hanoi(n, 1, 3, 2)
print(cnt)
for i in res:
    print(*i)
