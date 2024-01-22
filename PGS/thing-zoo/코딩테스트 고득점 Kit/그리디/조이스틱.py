def solution(name):
    answer = 0
    n = len(name)
    move = n - 1
    for i, ch in enumerate(name):
        # 상하이동 비교
        # A에서 이동횟수, Z에서 이동횟수(A->Z로 1칸 이동 필요)
        answer += min(ord(ch)-ord('A'), ord('Z')-ord(ch)+1)
        
        # 연속된 A 찾기
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
            
        # 좌우이동 비교
        # 기존이동수, 우측에서좌측, 좌측에서우측
        move = min([move, i*2+n-j, (n-j)*2+i])
    answer += move
    return answer