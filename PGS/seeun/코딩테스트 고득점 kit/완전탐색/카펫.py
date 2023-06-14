def solution(brown, yellow):
    answer = []
    total = brown + yellow # 총 카펫의 칸 수를 구함
    for i in range(2, int(total**0.5)+1): # 세로 길이가 가로길이보다 짧다고 주어졌으므로 제곱근까지만 탐색
        if total%i == 0: # 세로길이가 총 너비를 나누어떨어뜨리면
            b = i * 2 + ((total//i)-2)*2 # 갈색 카펫의 총 개수
            y = total - b # 노란색: 총 카펫 - 갈색 카펫
            if b == brown and y == yellow: # 주어진 개수와 같으면
                answer = [total//i, i] # 정답 저장 후 종료
                break
    return answer

b = 10
y = 2
print(solution(b, y))