number = input()
max_answer = '' # 최대 민겸수
current = '' # 현재 민겸숫자
for i in range(len(number)-1, -1, -1):
    if number[i] == 'K': # K의 경우
        max_answer = current + max_answer # 현재 민겸숫자를 더하고
        current = '5' # 5로 초기화
    else: # M의 경우
        if '5' in current: # MM..MK 인 경우 50..0이 최대
            current += '0' # 따라서 0을 더한다
        else: # MM..M 인 경우 11..1이 최대
            current += '1' # 따라서 1을 더한다
max_answer = current + max_answer

min_answer = '' # 최소 민겸수
current = '' # 현재 민겸숫자
for i in range(len(number)-1, -1, -1):
    if number[i] == 'K': # K의 경우 5가 최소
        min_answer = '5' + current + min_answer # 5랑 현재 민겸숫자를 더하고
        current = '' # 초기화
    else: # M의 경우
        if not current: # MM..M 인 경우 10..0이 최소
            current = '1'
        else:
            current += '0'
min_answer = current + min_answer
print(max_answer)
print(min_answer)