def solution(today, terms, privacies):
    answer = []
    # 약관 정보 추출
    terms_dic = {}
    for i in range(len(terms)):
        t, d = terms[i].split()
        terms_dic[t] = int(d)
    
    # 개인정보 별 확인
    for i in range(len(privacies)):
        d, t = privacies[i].split()
        y, m, d = map(int, d.split('.'))
        for _ in range(terms_dic[t]): # 유효기간만큼
            m += 1 # 달을 더하며
            if m > 12: # 12월이 넘으면
                m -= 12 # 1월부터 시작
                y += 1 # 1년 추가
        date = "%4d.%02d.%02d" %(y, m, d)
        if today >= date: # 오늘이 파기일 이후면
            answer.append(i+1) # 추가
                
    return answer