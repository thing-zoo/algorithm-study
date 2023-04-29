n = int(input())
tri_sum= []
for _ in range(n):
    tri_sum.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(tri_sum[i])):
        # [i][j] 값은 윗줄의 양쪽 두 수 중 큰 수에다가 더한다
        if j>=1 and j<len(tri_sum[i])-1:
            tri_sum[i][j] = max(tri_sum[i-1][j-1],tri_sum[i-1][j]) + tri_sum[i][j] 
        elif j<1:
            tri_sum[i][j] = tri_sum[i-1][j]+tri_sum[i][j]
        else:
            tri_sum[i][j] = tri_sum[i-1][j-1]+tri_sum[i][j]

print(max(tri_sum[n-1]))