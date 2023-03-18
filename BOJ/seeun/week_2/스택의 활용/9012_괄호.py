import sys
n = int(input())

def check(text):
    stack = []

    for i in text:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                if stack[len(stack)-1] == '(':
                    stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

for _ in range(n):
    text = sys.stdin.readline().rstrip()
    if len(text) % 2 == 0:
        if check(text) == True:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")