def solution(phone_book):# 나의 비루한 코드...
    # 모든 전화번호의 길이 파악
    sizes = []
    for p in phone_book:
        sizes.append(len(p))
    sizes = set(sizes) # 중복 제거
    
    d = {}
    for p in phone_book: # 전화번호별
        n = len(p)
        for s in sizes: # 모든 길이별로
            if n < s: continue
            pre = p[:s] # 접두사를 잘라서
            if pre not in d: # 사전에 넣기
                d[pre] = 1
            else:
                d[pre] += 1
    
    for p in phone_book: # 전화번호중에
        if d[p] > 1: # 접두사가 있다면
            return False
    return True

def solution2(phone_book): # 좀 더 세련된 다른분 코드...!
    answer = True
    hash_map = {}
    for phone_number in phone_book: # 미리 사전을 만들고
        hash_map[phone_number] = 1
    for phone_number in phone_book: 
        temp = ""
        for number in phone_number: # 한글자씩 추가하면서
            temp += number
            if temp in hash_map and temp != phone_number: #사전과 비교
                answer = False
    return answer
phone_book = ["1", "32", "33"]
print(solution(phone_book))