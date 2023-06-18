from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for num in permutations(range(len(dungeons)), len(dungeons)):
        energy = k
        cnt = 0
        for i in num:
            if energy-dungeons[i][1] < 0: # 현재 던전을 방문했을때 0이하가 되면 방문 안함
                continue
            if energy >= dungeons[i][0]: # 현재 피로도가 최소필요피로도 이상 있으면 -> 던전 방문 가능
                energy -= dungeons[i][1] # 피로도 감소
                cnt += 1 # 방문한 던전 개수 +1
        answer = max(answer, cnt) # 최댓값으로 정답 갱신   
    return answer

k, dungeons = 80,[[80,20],[50,40],[30,10]]
print(solution(k, dungeons))