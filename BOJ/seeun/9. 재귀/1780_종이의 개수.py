paper = []
one = 0
zero = 0
minusone = 0
def cut(i, j, n):
    global one, zero, minusone
    num = paper[i][j]
    idx = n//3
   
    for p in range(i, i+n):
        for q in range(j, j+n):
            if paper[p][q] != num:
                cut(i, j, n//3)
                cut(i, j+idx, n//3)
                cut(i, j+idx*2, n//3)
                cut(i+idx,j, n//3)
                cut(i+idx,j+idx, n//3)
                cut(i+idx,j+idx*2, n//3)
                cut(i+idx*2,j, n//3)
                cut(i+idx*2, j+idx, n//3)
                cut(i+idx*2, j+idx*2, n//3)
                return
    
    if num == 0:
        zero += 1
       
    elif num == 1:
        one += 1
      
    else:
        minusone += 1
       
n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))

cut(0, 0, n)
print(minusone)
print(zero)
print(one)