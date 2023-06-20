import math
def solution(n, k):
    answer = 0
    numlist = []
    tmp = ""
    while n > k:
        if n%k==0: # 0이 나오면 지금까지 만들어진 숫자를 리스트에 저장
            n //= k
            if tmp:
                numlist.append(tmp)
            tmp = ""
        else: # 나머지가 0이 아니면 계속 숫자를 앞에 추가해주기
            tmp = str(n%k) + tmp
            n //= k
    # 마지막에 남은 숫자 처리
    tmp = str(n%k) + tmp
    numlist.append(tmp)
    # 문자열 숫자를 정수로 변경
    numlist = list(map(int, numlist))
    
    # 소수 판별
    for k in numlist:
        flag = True
        if k == 1:
            continue
        for i in range(2, math.floor(k**0.5)+1):
            if k%i==0:
                flag = False
                break
        if flag:
            answer += 1
        
    return answer