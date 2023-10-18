import sys
input = sys.stdin.readline
S = input().rstrip()
tmp = "()[]"
while S!='.':
    stack = []
    for s in S:
        if s in tmp: # 괄호인 경우에만 스택에 넣기
            stack.append(s)
            if "".join(stack[-2:]) == "()" or "".join(stack[-2:]) == "[]": # 스택의 마지막에 완벽한 쌍이 있으면 pop
                stack.pop()
                stack.pop()
                
    if stack: 
        print('no')
    else: # 스택이 비어있으면 균형잡힌 세상임
        print('yes')
    S = input().rstrip()

