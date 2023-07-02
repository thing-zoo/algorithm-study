def solution(cookie):
    if len(cookie) == 1:
        return 0
    if len(cookie) == 2:
        if cookie[0] != cookie[1]:
            return 0
        else:
            return cookie[1]

    coosum = [0] * len(cookie)
    coosum[0] = cookie[0]
    for i in range(1, len(cookie)):
        coosum[i] += coosum[i-1] + cookie[i]
    
    answer = -1
    maxcookie = coosum[-1] //2 if coosum[-1] %2 == 0 else (coosum[-1]-1)//2
    for l in range(len(cookie)):
        for r in range(l+1, len(cookie)):
            # 토탈이 짝수이면 바구니 단위로 똑같이 나눌 수 있는지 봐야함
            total = coosum[r] - coosum[l] + cookie[l]
            if total % 2 == 1:
                continue

            for i in range(r-1, l-1, -1):
                if coosum[r] - coosum[i] > total //2:
                    break
                if (coosum[r] - coosum[i]) == total//2:
                    answer = max(answer, total//2)
                    if maxcookie == answer:
                        return answer
                    break
    
    if answer == -1:
        return 0
    else: return answer            
