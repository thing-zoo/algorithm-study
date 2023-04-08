def validation(code): # 암호 유효성 확인
    v = 0; c = 0
    for i in code:
       if i in vowel: # 모음 세기
          v += 1
       else: # 자음 세기
          c += 1
    if v >= 1 and c >= 2: # 모음 1개이상 자음 2개이상이면
       return True # 유효
    return False 
         
def f():
    if len(code) == l and validation(code):
        print("".join(code))
        return
    for i in data:
        if code and ord(code[-1]) > ord(i): # 사전순이 아니면
            continue # 건너뛰기
        if i not in code:
            code.append(i)
            f()
            code.pop() 
vowel = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
data = list(input().split())
data.sort()
code = []
f()