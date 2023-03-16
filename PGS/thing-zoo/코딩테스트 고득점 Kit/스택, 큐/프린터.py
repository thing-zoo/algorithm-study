def solution(priorities, location):
    answer = 0
    cur = location
    while priorities:
        back = False
        for i in range(1, len(priorities)):
            if priorities[0] < priorities[i]:
                back = True
                break
        if back:
            priorities.append(priorities.pop(0))
            cur -= 1
            if cur < 0: 
                cur = len(priorities) - 1
        else:
            priorities.pop(0)
            answer += 1
            if cur == 0:
                break
            cur -= 1
    return answer

p = [1, 1, 9, 1, 1, 1]
l = 0
print(solution(p, l))