for _ in range(int(input())):
    n = int(input())
    team = list(map(int, input().split()))
    
    # 팀 별 주자수 세기
    count = {}
    for i in range(n):
        if team[i] in count:
            count[team[i]] += 1
        else:
            count[team[i]] = 1

    # 점수 계산하기
    result = {}
    j = 1 # 점수
    for i in range(n):
        if count[team[i]] >= 6: # 주자수가 6명인 팀만
            if team[i] in result:
                if result[team[i]][0] < 4: # 상위 4명까지 계산
                    result[team[i]][0] += 1
                    result[team[i]][1] += j
                elif result[team[i]][0] == 4: # 동점 시 5번째 주자 점수 필요
                    result[team[i]][0] += 1
                    result[team[i]][2] = j
            else:
                result[team[i]] = [1, j, 0] # [현재인원수, 총점, 5번째 주자 점수]
            j += 1
    win = sorted(result.items(), key=lambda x: (x[1][1], x[1][2]))[0] # 우승팀 찾기
    print(win[0]) # 우승 팀 번호