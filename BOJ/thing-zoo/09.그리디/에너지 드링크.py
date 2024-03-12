n = int(input())
x = list(map(int, input().split()))
x.sort(reverse=True) # 내림차순 정렬
answer = x[0] # 최대값만 원래값 취하고
for i in range(1, n): # 나머지는
    answer += x[i]/2 # 절반씩 취한다
print(answer)