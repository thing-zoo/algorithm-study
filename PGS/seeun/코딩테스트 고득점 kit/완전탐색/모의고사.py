def solution(answers):
    answers = [1,2,3,4,5]
    answer = []
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    res = [[0, 0], [1,0], [2,0]]
    for i in range(len(answers)):
        i1 = i%len(ans1)
        i2 = i%len(ans2)
        i3 = i%len(ans3)
        if answers[i] == ans1[i1]:
            res[0][1] += 1
        if answers[i] == ans2[i2]:
            res[1][1] += 1
        if answers[i] == ans3[i3]:
            res[2][1] += 1
    
    res.sort(key=lambda x:-x[1])
    maxnum = res[0][1]
    answer.append(res[0][0]+1)
    for i in range(1, len(res)):
        if res[i][1] == maxnum:
            answer.append(res[i][0]+1)
    print(answer)
    answer.sort()
    return answer

solution([1,3,2,4,2])