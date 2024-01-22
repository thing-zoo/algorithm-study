exp = input()
stack = []
answer = ''
for e in exp:
    if e == '(':
        stack.append(e)
    elif e == ')':
        while stack and stack[-1] != '(': # 왼쪽괄호나올때까지
            answer += stack.pop() # 붙이기
        stack.pop()
    elif e == '*' or e == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'): # 곱하기거나 나누기면
            answer += stack.pop() # 붙이기
        stack.append(e)
    elif e == '+' or e == '-':
        while stack and stack[-1] != '(': # 괄호빼고 나머지면(+-*/)
            answer += stack.pop() # 붙이기
        stack.append(e)
    else: # 알파벳
        answer += e
while stack: # 남은거
    answer += stack.pop() # 붙이기
print(answer)