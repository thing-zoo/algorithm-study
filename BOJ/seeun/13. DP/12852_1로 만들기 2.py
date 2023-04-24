n = int(input())

d = [[0,1] for _ in range(n+1)]

# [i][0]: i가 되기 위해 최소 몇번의 연산을 거쳐야 하는지
# [i][1]: 최선의 연산을 하고 나면 어떤 숫자가 되는지 저장함(경로 추적용)
for i in range(2, n+1):
    d[i][0] = d[i-1][0]+1
    d[i][1] = i-1
    if i%2==0:
        if d[i][0] > d[int(i/2)][0]+1:
            d[i][0] = d[int(i/2)][0]+1
            d[i][1] = i/2
    if i%3 == 0:
        if d[i][0] > d[int(i/3)][0]+1:
            d[i][0] = d[int(i/3)][0]+1
            d[i][1] = i/3
print(d[n][0])
i = n
while i != 1:
    print(i, end=" ")
    i = int(d[i][1])
print(1)