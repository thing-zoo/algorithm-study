def solution(prices):
    answer = []
    
    # prices.reverse()
    for i in range(len(prices)-1):
        cnt = 1
        check = True
        for j in range(i+1, len(prices)-1):
            if prices[i]>prices[j]:
                answer.append(cnt)
                check = False
                break
            else:
                cnt += 1
        if check:
            answer.append(len(prices)-i-1)
    answer.append(0)
    return answer

prices = [5,4,3,2,1]	
print(solution(prices))