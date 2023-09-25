import re
def solution(str1, str2):
    answer = 0
    
    # 모두 대문자로 변경
    new1 = str1.upper()
    new2 = str2.upper()

    str1 = []
    str2 = []
    for i in range(2,len(new1)+1):
        tmp = re.sub(r"[^a-zA-Z]", "", new1[i-2:i]) # 두글자씩 끊어서 알파벳만 남김
        if len(tmp) == 2: # 특수문자나 공백, 숫자가 없는 문자열이면 배열에 저장
            str1.append(tmp)
            
    for i in range(2,len(new2)+1):
        tmp = re.sub(r"[^a-zA-Z]", "", new2[i-2:i])
        if len(tmp) == 2:
            str2.append(tmp)
            

    # 교집합
    inter = []
    str2_tmp = str2.copy()
    for s1 in str1:
        if s1 in str2_tmp: # 1에 있는 문자가 2에도 있으면
            str2_tmp.remove(s1) # 한번 검사한 문자는 지워줌
            inter.append(s1) # 교집합 배열에 추가
            
    
    # 합집합
    # 1 1 2   4 5
    # 1   2 3   5 6 7
    uni = str2.copy() # 합집합이기 때문에 2를 기본에 두고 시작함
    str2_tmp = str2.copy()
    for s1 in str1:
        if s1 not in str2_tmp: # 합집합이기 때문에 2에 없는 원소이면 추가해줌
            uni.append(s1)
        else: # 이미 있으면 검사한 원소는 삭제(겹치는 원소이므로 추가할 필요 없음)
            str2_tmp.remove(s1)
            
            
    if not uni:
        answer = 65536
    else:
        answer = len(inter)/len(uni) *65536
    
    return int(answer)