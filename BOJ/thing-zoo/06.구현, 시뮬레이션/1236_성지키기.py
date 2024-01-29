n, m = map(int, input().split())
check_i = [False]*n # 세로줄 경비원 존재 여부
check_j = [False]*m # 가로줄 경비원 존재 여부
for i in range(n):
    temp = input()
    for j in range(m):
        if temp[j] == 'X':
            check_j[j] = True
            check_i[i] = True
print(max(check_i.count(False), check_j.count(False))) # 둘중 최대값이 최소 경비원 수