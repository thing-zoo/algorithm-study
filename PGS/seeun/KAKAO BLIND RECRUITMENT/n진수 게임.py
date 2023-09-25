def solution(n, t, m, p):
    answer = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    numlist = []
    length = 0
    
    for i in range(n): # 초기 숫자 세팅
        numlist.append(nums[i])
        length += len(numlist[-1])
    
    i = 1 # i번째 숫자에 0~n까지 숫자를 더해서 n진수를 구함
    while length < t*m+1:
        for j in range(n):
            numlist.append(numlist[i]+nums[j])
            length += len(numlist[i]+nums[j])
        i += 1

    total = "".join(numlist) # 하나의 문자열로 변환
    
    for i in range(p-1, t*m, m): # 튜브가 말할 숫자만 골라서 더해줌
        answer += total[i]
    print(answer)
    return answer
    
solution(2, 4, 2, 1)