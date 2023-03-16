def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        sec = 0
        for j in range(i+1, n):
            sec += 1
            if prices[i] > prices[j]:
                break
        answer.append(sec)

    return answer

p = [1,2,3,2,3]
print(solution(p))