def solution(name):
    answer = 0
    move = len(name) - 1 # 우로만 이동횟수
    while name[move] == 'A' and move > 0: # A가 뒤에 있는 경우
        move -= 1
    if move < 0:
        return answer
    for i, ch in enumerate(name):
        # A에서 이동횟수, Z에서 이동횟수(A->Z로 1칸 이동 필요) 비교
        answer += min(ord(ch)-ord('A'), ord('Z')-ord(ch)+1)
        
        # A가 연속할 경우 좌우 이동 비교
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
        move = min(move, i*2 + len(name) - j)    
    answer += move
    return answer