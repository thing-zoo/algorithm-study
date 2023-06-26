def solution(m, musicinfos):
    answer = ''
    melody = {}
    for music in musicinfos:
        music = music.split(',')
        start = list(map(int, music[0].split(":")))
        end = list(map(int, music[1].split(':')))
        
        # 음악 재생 시간
        time = end[0]*60+end[1] - (start[0]*60+start[1])
        start = start[0]*60+start[1]
        
        # #붙은 음은 다른 글자 한글자로 치환
        music[3] = str(music[3])
        music[3] = music[3].replace("C#", '1')
        music[3] = music[3].replace("D#", '2')
        music[3] = music[3].replace("F#", '3')
        music[3] = music[3].replace("G#", '4')
        music[3] = music[3].replace("A#", '5')
        
        # 시작시간, 재생시간, 멜로디를 저장
        melody[music[2]] = [start, time, music[3]*(time//len(music[3])) + music[3][:time%len(music[3])+1]]
        

    candi = [] # 곡 후보 저장할 배열
    # 주어진 배열에서도 #을 한글자로 치환
    m = str(m)
    m = m.replace("C#", '1')
    m = m.replace("D#", '2')
    m = m.replace("F#", '3')
    m = m.replace("G#", '4')
    m = m.replace("A#", '5')
    
    for k in melody.keys():
        if m in melody[k][2]: # 곡의 멜로디에 주어진 멜로디가 포함되어 있으면
            candi.append([k, melody[k][1], melody[k][0]]) # 제목, 재생시간, 시작시간 저장
            
            
    if len(candi) == 1: # 한 개의 곡만 있으면
        answer = (candi[0][0])
    elif len(candi) > 1: # 한 개 이상의 곡이 있으면
        candi.sort(key = lambda x: (-x[1], x[2])) # 
        answer = (candi[0][0])
    else: # 일치하는 곡이 없으면
        answer = "(None)"
        
    return answer

print(solution("CC#BCC#BCC#BCC#B",	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))