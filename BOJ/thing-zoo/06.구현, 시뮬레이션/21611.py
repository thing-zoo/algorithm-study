dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

dr2 = [-1, 1, 0, 0]
dc2 = [0, 0, -1, 1]

def make2Dto1D(board): # 구슬 2차원배열을 1차원 배열로
    r = n // 2
    c = n // 2
    repeat = 1
    d = 0

    new_arr = []
    while True:
        for _ in range(2):
            for _ in range(repeat):  # repeat만큼 같은 방향으로 이동
                nr = r + dr[d]
                nc = c + dc[d]
                new_arr.append(board[nr][nc])
                if nr == nc == 0: return new_arr
                r = nr
                c = nc
            d = (d + 1) % 4  # 방향 바꾸기
        repeat += 1  # repeat 증가
def destory(board, d, s): # 명령에 따라 파괴하기
    r = n // 2
    c = n // 2
    for i in range(1, s+1):
        nr = r + dr2[d]*i
        nc = c + dc2[d]*i
        board[nr][nc] = 0

def move(arr): # 구슬 배열에서 빈칸 제거
    return [arr[i] for i in range(len(arr)) if arr[i] != 0]
def bomb(arr):
    while arr:
        flag = False # 폭발 여부
        pre = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == pre: # 같은 구슬이면
                count += 1
            else: # 다른 구슬이면
                if count >= 4: # 4개이상이면
                    for j in range(1, count+1): # 개수만큼
                        arr[i-j] = 0 # 폭발
                    answer[pre] += count # 구슬별 폭발 개수 세기
                    flag = True
                pre = arr[i]
                count = 1
        # 남아있다면 폭발
        if count >= 4:  # 4개이상이면
            for j in range(1, count + 1):  # 개수만큼
                arr[len(arr) - j] = 0  # 폭발
            answer[pre] += count  # 구슬별 폭발 개수 세기
            flag = True
        if not flag: break
        arr = move(arr)
    return arr
def transform(arr):
    if not arr: return []
    new_arr = []
    pre = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == pre:  # 같은 구슬이면
            count += 1
        else:  # 다른 구슬이면
            new_arr.append(count)
            new_arr.append(pre)

            pre = arr[i]
            count = 1

    # 마지막 요소
    new_arr.append(count)
    new_arr.append(pre)

    return new_arr

def make1Dto2D(arr): # 구슬 1차원배열을 2차원 배열로
    r = n // 2
    c = n // 2
    repeat = 1
    d = 0
    i = 0

    flag = True
    new_board = [[0]*n for _ in range(n)]
    if not arr: return new_board
    while flag:
        for _ in range(2):
            for _ in range(repeat):  # repeat만큼 같은 방향으로 이동
                nr = r + dr[d]
                nc = c + dc[d]
                new_board[nr][nc] = arr[i]
                if nr == nc == 0 or i == len(arr)-1:
                    flag = False
                    break
                r = nr
                c = nc
                i += 1
            d = (d + 1) % 4  # 방향 바꾸기
            if not flag: break
        repeat += 1  # repeat 증가
    return new_board

def print_board():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
arr = make2Dto1D(board)

answer = [0]*4
for i in range(m):
    d, s = map(int, input().split())
    destory(board, d-1, s)
    arr = make2Dto1D(board)
    arr = move(arr)
    arr = bomb(arr)
    arr = transform(arr)
    board = make1Dto2D(arr)

print(answer[1]+2*answer[2]+3*answer[3])