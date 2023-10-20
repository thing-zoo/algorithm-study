def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for r in range(2, total+1):
        c = total//r
        if r < c: continue # 가로 >= 세로
        if 2*(r+c) - 4 == brown: # 갈색은 둘레의 길이
            answer = [r, c]
            break
            
    return answer