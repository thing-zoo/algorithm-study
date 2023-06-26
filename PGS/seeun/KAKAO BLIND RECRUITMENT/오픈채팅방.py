def solution(record):
    answer = []
    log = [] # 입퇴장 로그 기록
    id_name = {} # 아이디 별 닉네임 변경
    
    for r in record:
        r = r.split()
        if r[0] != 'Leave': # 입장 Or 변경: 닉네임 갱신 가능
            id_name[r[1]] = r[2] # 키: 아이디, 값: 닉네임
            
        if r[0] != 'Change': # 입/퇴장만 기록함
            log.append((r[0], r[1]))
        
    for l in log: # 로그를 돌면서 최종 닉네임으로 출력
        if l[0] == 'Enter':
            answer.append(id_name[l[1]] + '님이 들어왔습니다.')
        else:
            answer.append(id_name[l[1]] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))