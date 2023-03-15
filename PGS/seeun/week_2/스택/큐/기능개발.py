import math
def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        queue.append(day)
        
    maxday = queue[0]
    sum = 0
    print(queue)
    for i in queue:
        if maxday<i:
            maxday = i
            answer.append(sum)
            sum = 1
        else:
            sum += 1
    answer.append(sum)

    return answer