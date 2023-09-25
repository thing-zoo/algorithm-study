from collections import defaultdict
def solution(gems):
    answer = [0, len(gems)]
    vari = len(set(gems)) # 보석 종류 개수
    bag = {gems[0]:1,} # 현재 가방에 넣은 보석 종류들
    i,j = 0, 0
    print(vari)
    while i < len(gems) and j < len(gems):
        if len(bag) < vari: # 아직 종류가 다 없으면
            j += 1 # 오른쪽 포인터 이동
            if j == len(gems): # 끝까지 가버렸으면 종료
                break
            bag[gems[j]] = bag.get(gems[j], 0) +1 # 보석 가방에 넣기
        else: # 종류대로 가방에 넣었으면
            if (answer[1]-answer[0]+1) > (j-i+1): # 더 짧은 구간이 있으면 갱신
                answer = [i+1, j+1]
                
            # 왼쪽 포인터의 보석을 가방에서 빼기
            if bag[gems[i]] == 1: 
                del bag[gems[i]]
            else:
                bag[gems[i]] -= 1
            i += 1
        print(i, j, answer, bag)
                    
    return answer

print(solution(["AA", "AB", "AC", "AA", "AC"]))
