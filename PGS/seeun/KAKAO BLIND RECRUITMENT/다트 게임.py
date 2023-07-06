import re
def solution(dartResult):
    answer = 0
    score = [0] * len(dartResult) # 점수를 저장
    pm = [1] * len(dartResult) # +-를 저장
    dartResult = list(dartResult)

    i = 0 # dartResult 인덱스
    j = 0 # score, pm용 인덱스
    while i < len(dartResult):
        if dartResult[i] in '12345678910':
            if dartResult[i+1] == '0': # 점수가 10점인 경우
                score[j] = int("".join(dartResult[i:i+2]))
                i += 1
            else:
                score[j] = int(dartResult[i])
            
            # 보너스 계산
            if dartResult[i+1] == "D":
                score[j] = score[j] * score[j]
            elif dartResult[i+1] == "T":
                score[j] = score[j] * score[j] * score[j]
            
            # 옵션이 있으면 옵션 계산
            if i+2 < len(dartResult) and dartResult[i+2] == "*":
                score[j] *= 2
                if j > 0:
                    score[j-1] *= 2
                i +=3
            elif i+2 < len(dartResult) and dartResult[i+2] == "#":
                pm[j] = -1

                i +=3
            else: # 옵션이 없으면 인덱스 2개만 이동
                i += 2

            j += 1

    for i in range(j):
        answer += score[i]*pm[i] # 부호와 점수를 곱해서 더하기
    return answer

print(solution("1D2S#10S"))