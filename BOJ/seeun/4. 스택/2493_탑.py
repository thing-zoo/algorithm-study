import sys
n = int(input())
tower = list(map(int, sys.stdin.readline().split()))
res = [0] * n

h_stack = [] #height
num_stack = [] #number of tower

i = 0
while True:
    if len(h_stack) == 0:
        h_stack.append(tower[i])
        num_stack.append(i)
    elif h_stack[len(num_stack)-1] < tower[i]:
        while h_stack[len(num_stack)-1] < tower[i]:
            num_stack.pop()
            h_stack.pop()
            if len(h_stack) == 0: break
        if len(h_stack)!=0:
            res[i] = num_stack[len(num_stack)-1]+1
        h_stack.append(tower[i])
        num_stack.append(i)

    elif h_stack[len(num_stack)-1] > tower[i]:
        res[i] = num_stack[len(num_stack)-1]+1
        h_stack.append(tower[i])
        num_stack.append(i)
    i += 1
    if i==n: break
   
print(*res)