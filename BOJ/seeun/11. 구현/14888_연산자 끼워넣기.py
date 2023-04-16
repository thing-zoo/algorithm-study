# 0:+
# 1:-
# 2:*
# 3://

def operate(res, num, op):
    if op == 0:
        res += nums[num]
    elif op == 1:
        res -= nums[num]
    elif op == 2:
        res *= nums[num]
    else:
        if res<0:
            res *= -1
            res = int(res/nums[num])
            res *= -1
        else:
            res = int(res/nums[num])
    return res

def dfs(num, res):
    global minanswer, maxanswer, visited
    if num == n-1:
        minanswer = min(minanswer, res)
        maxanswer = max(maxanswer, res)
        return
    for i in range( len(operators)):
        if not visited[i]:
            visited[i] = True
            res = operate(res, num+1,  operators[i])
           
            dfs(num+1, res)

            res = operate(res, num+1, operators_back[operators[i]]) # res 한단계 전으로 되돌리기
            visited[i] = False

n = int(input())
nums = list(map(int, input().split()))
operators_n = list(map(int, input().split()))
operators = []
for i in range(len(operators_n)):
    for j in range(operators_n[i]):
        operators.append(i)

visited = [False]*len(operators)
operators_back = [1, 0, 3, 2]
res = nums[0]
minanswer = 9999999999
maxanswer = -9999999999

dfs(0, res)
print(maxanswer, minanswer, sep="\n")