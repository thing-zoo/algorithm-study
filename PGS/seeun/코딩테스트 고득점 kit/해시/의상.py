from itertools import combinations
def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
            
    for v in dic.values():
        answer *= (v+1) # 현재 의상 종류의 가짓수 + 안입는 경우
    
    return answer-1 # 모든 경우를 곱하고 아무것도 안입는 경우만 빼줌