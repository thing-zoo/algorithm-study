from itertools import combinations
exp = input()
pos = [] # 괄호쌍 위치 저장
stack = []
for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        pos.append((stack.pop(), i))

answer = []
n = len(pos)
for i in range(1, n+1):
    for selected in combinations(range(n), i): # 경우의 수
        temp = list(exp)
        for j in selected: # 괄호 제거
            temp[pos[j][0]] = ''
            temp[pos[j][1]] = ''
        temp = ''.join(temp)
        if temp not in answer: # 중복 제거
            answer.append(temp)
answer.sort() # 사전순 정렬
print('\n'.join(answer))