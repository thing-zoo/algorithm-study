def solution(triangle):
    answer = 0
    h = len(triangle)
    for i in range(1, h):
        for j in range(len(triangle[i])):
            if j == 0: # 첫번째이면 무조건 오른쪽 위 숫자에서내려옴
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1: # 마지막이면 무조건 왼쪽 위 숫자에서 내려옴
                triangle[i][j] += triangle[i-1][j-1]
            else: # 위의 두 숫자 중에서 큰 숫자로 더하기
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[h-1])
    return answer