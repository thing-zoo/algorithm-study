import math
n, maxi = map(int, input().split())
girls = [0, 0, 0, 0, 0, 0]
boys = [0, 0, 0, 0, 0, 0]
for i in range(n):
    sex, grade =  map(int, input().split())
    if sex==0:
        girls[grade-1] += 1
    else:
        boys[grade-1] += 1

cnt = 0
for i in range(6):
    cnt += math.ceil(girls[i]/maxi)
    cnt += math.ceil(boys[i]/maxi)

print(cnt)