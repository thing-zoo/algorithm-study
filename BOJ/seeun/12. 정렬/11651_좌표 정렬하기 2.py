n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
   

xy.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
    print(*xy[i])