def solution(targets):
    answer = 0
    targets.sort()
    shoot = 0 # 요격할 포인트
    
    for t in targets:
        if shoot > t[0]: # 미사일 시작 위치가 요격포인트 이전이면
            shoot = min(shoot, t[1]) # 미사일 끝 vs 요격포인트 중 더 작은 값으로
        else: # 미사일 시작 위치가 요격포인트 이후이면 하나 쏘고 새로운 요격포인트 잡아야됨
            answer += 1 
            shoot = t[1] # 새로운 요격 포인트: 현재 미사일의 끝점
       
    return answer