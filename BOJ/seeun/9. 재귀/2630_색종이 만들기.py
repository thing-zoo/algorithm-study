paper = []
white = 0
blue = 0
def cut(i, j, n):
    global white, blue
    color = paper[i][j]
    for p in range(i, i+n):
        for q in range(j, j+n):
            if paper[p][q] != color:
                cut(i, j, n//2)
                cut(i, j+n//2, n//2)
                cut(i+n//2, j, n//2)
                cut(i+n//2, j+n//2, n//2)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

   
n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))

cut(0, 0, n)
print(white)
print(blue)