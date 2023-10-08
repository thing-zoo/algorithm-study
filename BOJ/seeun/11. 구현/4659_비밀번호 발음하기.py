import sys
input = sys.stdin.readline
molist = ['a', 'e', 'i', 'o', 'u']

pw = input().strip()
while pw != 'end':
    pw = list(pw)
    mo = 0 # 모음 개수
    ja_cnt = 0 # 연속된 자음 개수
    mo_cnt = 0 # 연속된 모음 개수
    prev = '' # 이전 문자
    acceptable = True

    for i in pw:
        if i in molist: # 모음일때
            if i != prev or (prev == 'o' and i == 'o') or (prev == 'e' and i=='e'): # 이전과 다르거나 ee, oo만 허용
                mo += 1 # 모음 개수 +1
                prev = i # 이전 문자 저장
                mo_cnt += 1 # 연속된 모음 개수 +1
                ja_cnt = 0 # 연속된 자음 개수 0
            else: # 같은 문자가 연속되면 종료
                acceptable = False
                break
        else: # 자음일때
            if i != prev: # 이전 글자와 다르면
                prev = i
                ja_cnt += 1
                mo_cnt = 0
            else:
                acceptable = False
                break
        
        if mo_cnt == 3 or ja_cnt == 3:
            acceptable = False
            break

    if acceptable and mo: # 허용된 문자열이고 모음을 포함하고 있으면
        print("<", "".join(pw), ">", " is acceptable.", sep="")
    else:
        print("<", "".join(pw), ">", " is not acceptable.", sep="")
    pw = input().strip()