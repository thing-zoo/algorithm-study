def transform(key): # 주어진 키를 표로 변환
    table = []
    # 키에서 알파벳 순서대로 중복 없이 삽입
    for i in key:
        if i not in table:
            table.append(i)
    # 키에 없는 알파벳 순서대로 삽입
    for i in range(ord('A'), ord('A')+26):
        if chr(i) == 'J': continue
        if chr(i) not in table:
            table.append(chr(i))
    return table

def seperate(message): # 주어진 메세지를 두글자씩 맞춰주기
    i = 0
    size = len(message)
    while i < size:
        if i == size-1: # 마지막 문자가 하나면
            message += 'X' # X 추가
        elif message[i] == message[i+1]: # 서로 같은문자면
            if message[i] != 'X': temp = 'X' # X 삽입
            else: temp = 'Q' # XX면 Q 삽입
            message = message[:i+1] + temp + message[i+1:]
            size += 1
        i += 2
        
    return message

def find(ch): # 표에서 ch의 행, 열 찾기
    for i in range(25):
        if key[i] == ch:
            return i//5, i%5

def encrypt(message): # 암호화
    for i in range(0, len(message), 2):
        a, b = find(message[i])
        c, d = find(message[i+1])
        if a == c: # 같은 행이면
            # 오른쪽으로 한칸 이동
            b = (b+1)%5
            d = (d+1)%5
        elif b == d: # 같은 열이면
            # 아래쪽으로 한칸 이동
            a = (a+1)%5
            c = (c+1)%5
        else: # 서로 다른 행,열이면
            b, d = d, b # 열 교환
        message[i] = key[a*5+b]
        message[i+1] = key[c*5+d]
    return ''.join(message)

message = input()
key = input()
key = transform(key)
message = seperate(message)
print(encrypt(list(message)))