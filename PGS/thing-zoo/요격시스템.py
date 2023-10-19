def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1]) # e 기준 오름차순
    end = -1 # 이전 e 값
    for s, e in targets:
        if end <= s: # 겹치지 않으면
            end = e
            answer += 1
    return answer