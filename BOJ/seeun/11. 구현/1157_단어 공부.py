string = input()
string = string.upper()
dic = {} # 알파벳 별 개수 카운트
for s in string:
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

maxvalue = max(dic.values()) # 최댓값 구하기
if list(dic.values()).count(maxvalue) > 1: # 최댓값이 여러개이면 바로 ? 출력
    print('?')
else:
    key = max(dic, key = dic.get) # 최댓값의 키값 출력
    print(key)