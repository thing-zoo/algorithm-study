def solution(today, terms, privacies):
    answer = []
    termsdic = {}

    # 약관 종류별 유효기간을 딕셔너리로 저장
    for i in range(len(terms)):
        t, n = terms[i].split()
        termsdic[t] = int(n)
    
    # 오늘 날짜를 하나의 숫자로 변환
    today = today.split('.')
    today = int(today[0])*10000 + int(today[1])*100 + int(today[2])

    # 번호별 파기 여부 결정
    for i in range(len(privacies)):
        date, typ = privacies[i].split()
        date = date.split('.')
        date = list(map(int, date))
        
        # 수집일자에 유효기간 더하기
        date[1] += termsdic[typ]
        
        # 12개월 지날 때 마다 1년 더해주기, 12월 보다 작아지면 종료
        while date[1] > 12:
            date[1] -= 12
            date[0] += 1        
        
        # 하루 빼기
        if date[2] - 1 == 0: # 하루 전날이 이전달인 경우
            date[2] = 28 # 이전달의 마지막날로 설정
            if date[1] - 1 == 0: # 이전달이 작년인 경우
                date[1] = 12 # 작년 12월로 설정
                date[0] -= 1 # 한해 빼기
            else:
                date[1] -= 1 # 그냥 이전달로 설정
        else:
            date[2] -= 1 # 그냥 하루 전날로 설정
        
        # 유효기간을 하나의 숫자로 변환
        tmp = date[0]*10000 + date[1]*100 + date[2]
        if tmp < today: # 만료날짜가 오늘 이전이면 파기 해야함
            answer.append(i+1)
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))