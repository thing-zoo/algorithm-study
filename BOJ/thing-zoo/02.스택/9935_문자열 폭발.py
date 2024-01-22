data = list(reversed(input()))
bomb = list(input())
while True:
    stack = []
    flag = False # 폭발 여부
    while data: # 앞에서부터
        stack.append(data.pop()) # 일단 넣는다
        if stack[-len(bomb):] == bomb: # 마지막부분이 폭발 문자열과 일치하면
            flag = True
            for _ in range(len(bomb)): # 폭발시킴
                stack.pop()
    data = stack[::-1] # 남은 문자열로 갱신
    if not flag: break # 폭발 없으면 종료
print(''.join(data[::-1]) if data else 'FRULA')