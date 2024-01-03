def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    depart = 540
    gone = 0 # 지금 갈사람
    for _ in range(n): # 마지막 n번째 운행할 때 콘이 타야됨
        cnt = 0 # 현재 셔틀에 탄 사람 수
        i = gone
        for i in range(gone, min(gone+m, len(timetable))): # m명 태우기
            time = int("".join(timetable[i][:2])) * 60 + int("".join(timetable[i][3:5]))
            if time <= depart: # 셔틀 출발 이전에 도착해서 기다리고 있는 사람이면 태움
                cnt += 1
            else:
                break
        gone += cnt # 다음에 탈 사람

        if _ == n-1 and cnt >= m: # 마지막 셔틀인데 정원 가득 차면 마지막 사람 도착시간 1분전에 도착
            answer = int("".join(timetable[gone-1][:2])) * 60 + int("".join(timetable[gone-1][3:5])) -1
        elif _ == n-1 and cnt < m: # 마지막 셔틀인데 빈자리 있으면 버스 오는 시간에 나가면 됨
            answer  = depart
            
        depart += t # 다음 셔틀 시간
    
    # 정답 시간 계산
    minu = answer%60
    hour = answer //60
    if hour < 10:
        hour = "0"+ str(hour)
    if minu < 10:
        minu = "0"+ str(minu)
    hour = str(hour)
    minu = str(minu)
    answer = hour + ":" + minu
    
    return answer