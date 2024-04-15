# 반복문 풀이
n = int(input())
size = 4*(n-1)+1
answer = ['' for _ in range(size)]
for i in range(size//2+1):
    if i%2 == 0:
        j = i//2 + 1
        answer[i] = answer[size-1-i] = '* '*(j-1) + '*'*(4*(n-j)+1) + ' *'*(j-1)
    else:
        j = i//2 + 1
        answer[i] = answer[size-1-i] = '* '*j + ' '*(size-4*j) + ' *'*j
        
for i in range(size):
    print(answer[i])
    
# 재귀 풀이
def draw(x, y, n):
    if n == 1:
        answer[x][y] = '*'
        return
    size = 4*(n-1)+1
    for i in range(size):
        answer[x][y+i] = answer[x+i][y] = answer[x+i][y+size-1] = answer[x+size-1][y+i] = '*'
    draw(x+2, y+2, n-1)
        
n = int(input())
size = 4*(n-1)+1
answer = [[' ']*size for _ in range(size)]
draw(0, 0, n)
for i in range(size):
    print(''.join(answer[i]))