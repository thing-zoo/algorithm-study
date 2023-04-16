def rotate(sticker): # 스티커 배열을 회전시키는 함수
    r, c = sticker[0]
    temp = sticker[1]
    rotated = [[0]*10 for _ in range(10)]
    for i in range(r):
        for j in range(c):
            rotated[j][r-i-1] = temp[i][j]
    return [c, r], rotated
    
def check(sticker, x, y): # 스티커를 붙일 수 있는지 확인하는 함수
    r, c = sticker[0]
    temp = sticker[1]
    if x + r > n or y + c > m:
        return False
    for i in range(r):
        for j in range(c):
            if temp[i][j] and laptop[x+i][y+j]: # 스티커 자리에 이미 다른스티커가 붙어있다면
                return False # 불가능
    return True

def put(sticker, x, y): # 스티커를 붙이는 함수
    r, c = sticker[0]
    temp = sticker[1]
    for i in range(r):
        for j in range(c):
            if temp[i][j]:
                laptop[x+i][y+j] = 1

def count(): # 스티커 개수 세는 함수
    answer = 0
    for i in range(n):
        for j in range(m):
            if laptop[i][j]:
                answer += 1
    return answer

def f(sticker):
    for i in range(n):   # 모든 칸에 대해
        for j in range(m):
            if check(sticker, i, j): # 붙일 수 있는지 확인
                put(sticker, i, j) # 붙이기
                return True
    return False

def solution():
    for sticker in stickers: # 모든 스티커에 대해
        r = 0
        while r < 4: 
            if f(sticker): # 붙였다면
                break
            else: # 못 붙였다면
                sticker = rotate(sticker) # 회전
                r += 1
    print(count())

n, m, k = map(int, input().split())
laptop = [[0]*m for _ in range(n)]
stickers = []

for _ in range(k):
    r,c = map(int, input().split())
    sticker = [[0]*10 for _ in range(10)] # 회전할때 인덱스 에러를 막기 위해 10*10으로 초기화
    for i in range(r):
        tmp = list(map(int, input().split()))
        for j in range(c):
            sticker[i][j] = tmp[j]
    stickers.append([[r,c],sticker])
solution()