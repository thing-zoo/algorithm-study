import sys 
n = int(input())

def check(text):
    stack = []
    for i in text:
        if len(stack) != 0:
            if stack[len(stack)-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else: stack.append(i)
    
    if len(stack) == 0:
        return True
    else:
        return False

sum = 0
for _ in range(n):
    text = sys.stdin.readline().rstrip()
    if len(text)%2 == 0:
        if check(text) == True:
            sum += 1

print(sum)