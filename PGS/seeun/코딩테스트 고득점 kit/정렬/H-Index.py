def solution(citations):
    answer = 0
    citations.sort()
    for i in range(citations[-1]): # 제일 큰 숫자까지만 검사
        up = 0
        for j in range(len(citations)): # 논문 인용 횟수 검사
            if citations[j] >= i: # i번 이상 인용된 논문
                up += 1
        if up >= i: # i개 이상이면
            answer = max(answer, i) # 정답 갱신
    return answer