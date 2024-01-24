from itertools import combinations
expr = list(input())
cnt = expr.count('(')
loc = [] # 괄호 세트 위치 저장
stack = []
for i in range(len(expr)): # 괄호 세트 위치 알아내기
    if expr[i] == '(':
        stack.append(i)
    elif expr[i] == ')':
        tmp = stack.pop()
        loc.append([tmp, i]) # 괄호 한 세트 위치 저장

res = set() # 중복을 제거하기 위해 set으로
for i in range(1, cnt+1): # 괄호 몇 세트 없앨지
    stack = []
    for location in combinations(loc, i): # 괄호 세트를 i개 뽑기
        dele = []
        for l in location: # 출력하지 않을 괄호 세트 위치
            dele.append(l[0])
            dele.append(l[1])
        tmp = ''
        for j in range(len(expr)):
            if j not in dele: # 삭제할 위치가 아니면 출력
                tmp += expr[j]
        res.add(tmp)

res = list(res)
res.sort() # 사전 순으로 정렬
print("\n".join(res))