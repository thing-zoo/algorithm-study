def solution(n, lost, reserve):
    answer = 0
    
    stu = [1] * (n+1)
    for i in range(len(lost)):
        stu[lost[i]] -=1
    for i in range(len(reserve)):
        stu[reserve[i]] += 1
    
    # 빌려주기전 체육을 할 수 있는 학생 수
    cnt = n-stu.count(0)
    for i in range(1, n+1):
        if stu[i] == 0: # i가 체육복이 없으면
            if i-1>0 and stu[i-1] == 2: # 앞사람한테 빌릴 수 있는지
                stu[i-1] -= 1
                stu[i] += 1
                cnt += 1
            elif i+1<=n and stu[i+1] == 2: # 뒷사람한테 빌릴수 있는지
                stu[i+1] -=1
                stu[i] += 1
                cnt += 1

    print(cnt)
    answer = cnt
    return answer