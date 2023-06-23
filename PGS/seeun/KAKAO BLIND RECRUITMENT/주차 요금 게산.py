import math
def solution(fees, records):
    answer = []
    inout = {} # 입출차 상태와 시간 저장
    fee = {} # 요금 계산을 위한 시간 저장
    
    for r in records:
        r = r.split()
        if r[2] == "IN": # 입차인 경우
            if r[1] in inout.keys(): # 한번 들어온 기록이 있는 차량
                inout[r[1]] = [True, r[0]]

            else: # 한번도 들어온적 없는 차량
                inout[r[1]] = [True, r[0]]
                fee[r[1]] = 0
            
        else: # 출차: 시간계산해야됨
            intime = list(map(int, inout[r[1]][1].split(':')))
            intime = intime[0]*60+intime[1] # 분으로 변환
            outtime = list(map(int, r[0].split(':')))
            outtime = outtime[0]*60+outtime[1] # 분으로 변환

            fee[r[1]] += (outtime-intime)
            inout[r[1]] = [False, r[0]] # 출차로 저장
 
    # 요금 계산
    for k in inout.keys():
        # 아직 안나간차이면 23:59에 나간걸로 처리
        if inout[k][0] == True: 
            intime = list(map(int, inout[k][1].split(':')))
            intime = intime[0]*60+intime[1] # 분으로 계산
            outtime = 23*60+59
            fee[k] += outtime-intime

        # 기본시간 이내이면 기본요금
        if fee[k] < fees[0]:
            fee[k] = fees[1]
        else:
            fee[k] -= fees[0]
            fee[k] = math.ceil(fee[k] / fees[2])*fees[3] + fees[1] # 단위시간으로 나눔*단위요금 + 기본요금
    
    # 차량 번호 기준으로 정렬
    answer = sorted(list(fee.items()), key=lambda x:x[0])
    answer = [n[1] for n in answer]
    return answer