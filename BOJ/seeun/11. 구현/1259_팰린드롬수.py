test = input()
while test != '0':
    m = len(test)//2
    rev = test[::-1] # 문자열 뒤집기
    if test[:m+1] == rev[:m+1]:
        print('yes')
    else:
        print('no')
    
    test = input()