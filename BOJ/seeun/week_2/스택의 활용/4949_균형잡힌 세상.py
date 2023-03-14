import sys, re
text = []

def check(text):
    stack = []
    i = 0
    for i in text:
        if i == '(' or i == '[':
            stack.append(i)
        elif len(stack) == 0: return False #닫는 괄호는 있는데 스택에 남은게 없다면 False
        elif i == ')':
            if stack[len(stack)-1] == '(':
                stack.pop()
            else:
                return False
        elif  i == ']':
            if stack[len(stack)-1] == '[':
                stack.pop()
            else:
                return False
    if len(stack)!=0: #닫는괄호는 없는데 스택에 남아있으면
        return False
    else: return True
    
text = sys.stdin.readline().rstrip()
new = []
while text != ".":
    new = re.sub('[a-zA-Z0-9.]', '', text).replace(" ", "")
    if check(new) == True:
        print("yes")
    else:
        print("no")
    text = sys.stdin.readline().rstrip()
    # text = input()