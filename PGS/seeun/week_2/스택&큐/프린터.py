def solution(priorities, location): 
    answer = 0
    mynum = priorities[location]
    maxpri = max(priorities)
    while True:
        # 더 큰수가 없고 제일 앞에 있는 수가 내가 요청한 수면
        # 만약에 같은수가 또 있으면..?
        if len(priorities)-1 == 0:
            break
        if maxpri == mynum and location == 0: # 내가 찾는 수가 제일 높은 우선순위 & 제일 앞에 있으면
            break
        elif priorities[0] == maxpri: #최대값이 젤 앞에 있으면 없애고 프린트 순서+1, 최대값 갱신
            del priorities[0]
            answer += 1
            if maxpri != max(priorities): # 지금 최대값이랑 다음 최대값이랑 다르면 갱신
                maxpri = max(priorities)
            location -= 1
        else: #암것도 아니면 그냥 제일 뒷 순서로 보내기
            priorities.append(priorities[0])
            del priorities[0]
            location -= 1

        if location < 0: # 뒤로가면 양수로 바꿔주기
            location = len(priorities)-1

    answer = answer+1
    return answer

priorities = [2, 1, 3, 2]
location = 2


print(solution(priorities, location))
