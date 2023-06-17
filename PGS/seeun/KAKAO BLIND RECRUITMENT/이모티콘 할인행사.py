from itertools import product # 중복순열 라이브러리
def solution(users, emoticons):
    answer = []
    plus, money = 0, 0 

    # 얼마를 할인 했을지는 모름 내가 하나하나 넣어보고 최대 이득을 출력해야됨
    for p in product([10, 20, 30, 40], repeat = len(emoticons)): # 이모티콘들의 할인율 조합
        buy = [0]*len(users) # 이 할인율로 사람들이 얼마를 쓸지
        for i in range(len(emoticons)): # i번 이모티콘을 p[i]할인율을 적용해서 살건지
            for j in range(len(users)): # 사람마다 조사
                if users[j][0] <= p[i]: # 원하는 할인율 이상 할인하면
                    buy[j] += emoticons[i]*(100-p[i])*0.01 # 할인된 가겨으로 구매

        # 모든 이모티콘을 해당 할인율로 할인 했을 때 살말 조사했으면
        tmpplus = 0
        for i in range(len(users)):
            if buy[i] >= users[i][1]:
                tmpplus += 1
                buy[i] = 0

        # 구독자와 판매액 갱신
        if plus < tmpplus: # 현재 할인율에서 구독자가 더 증가한다면
            plus = tmpplus # 구독자 갱신
            money = sum(buy) # 판매액 갱신
        elif plus == tmpplus: # 구독자가 최댓값이랑 똑같다면 판매액이 더 큰 할인율 선택
            money = max(sum(buy), money)

    answer = [plus, int(money)]
    return answer