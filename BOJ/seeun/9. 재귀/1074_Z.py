cnt = 0
def check(i,j, num, n):
    global cnt, r, c
    if n == 2: #2*2 일때 +0, 1, 2, 3 중에 하나 하고 리턴
        if i == r and j == c:
            cnt += 0
            return
        elif i == r and j + 1 == c:
            cnt += 1
            return
        elif i+1 == r and j == c:
            cnt += 2
            return
        elif i+1 == r and j +1 == c:
            cnt += 3
            return
    num -=1

    if i<= r <i+n//2 and j<= c <j+n//2: # 1번째
        cnt += 0
        check(i, j, num, n//2)
    elif i<= r <i+n//2 and j+n//2<= c <j+n: #2번째
        cnt += 2**(2*(num)) # 1면 개수만큼 카운트 증가
        check(i, j+n//2, num,  n//2)
    elif i+n//2<= r <i+n and j<= c <j+n//2: #3번째
        cnt += 2**(2*(num))*2 # 2면 개수만큼 카운트 증가
        check(i+n//2, j, num,  n//2) 
    elif i+n//2<= r <i+n and j+n//2<= c <j+n: #4번째
        cnt += 2**(2*(num))*3 # 3면 개수만큼 카운트 증가 
        check(i+n//2, j+n//2, num, n//2)


n, r, c = map(int, input().split())
num = n
n = 2**n
check(0, 0, num, n)
print(cnt)