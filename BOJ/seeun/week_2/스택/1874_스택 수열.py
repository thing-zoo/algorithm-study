import sys
n = int(input())

stack = [1]
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

i = 0
stack_i = 2
res = ["+"]
while True:

    if len(stack) == 0: #아무것도 없으면 push
        stack.append(stack_i)
        res.append("+")
        stack_i += 1
    elif stack[len(stack)-1] == nums[i]: #뽑아낼 숫자 == 스택 top 이면 pop
        stack.pop()
        res.append("-")
        i += 1
    else: # 그 외 상황이면 순서대로 push
        stack.append(stack_i)
        res.append("+")
        stack_i += 1

    if stack_i == n+1: #입력받은 숫자 만큼 push가 다 되었으면 종료
        break 

tmp = nums[i:]
tmp.reverse()

# 스택에 남은 숫자와 남은 수열이 같으면 성공
# 남은 수열이 내림차순이 아니면 실패 -> pop 밖에 못하기 때문
if stack != tmp:
    print("NO")
else:
    print(*res, sep="\n")
    while len(stack)>0:
        stack.pop()
        print('-')
