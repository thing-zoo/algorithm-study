from collections import defaultdict
def solution(survey, choices):
    answer = ''
    res = defaultdict(int)

    for i in range(len(survey)):
        if choices[i] < 4: # 답변이 4 미만이면 앞자리 유형에 점수
            res[survey[i][0]] += 4-choices[i]
        elif choices[i] > 4: # 4보다 크면 뒷자리 유형에 점수
            res[survey[i][1]] += choices[i] - 4
      
    if res['R'] > res['T']:
        answer += "R"
    elif res['R'] < res['T']:
        answer += "T"
    else:
        answer += "R"
        
    if res['C'] > res['F']:
        answer += "C"
    elif res['C'] < res['F']:
        answer += "F"
    else:
        answer += "C"
        
    if res['J'] > res['M']:
        answer += "J"
    elif res['J'] < res['M']:
        answer += "M"
    else:
        answer += "J"
        
    if res['A'] > res['N']:
        answer += "A"
    elif res['A'] < res['N']:
        answer += "N"
    else:
        answer += "A"
        
    return answer