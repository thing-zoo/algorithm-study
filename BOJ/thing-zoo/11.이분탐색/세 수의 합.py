# a[x]+a[y]+a[z] = a[k]이면 a[x]+a[y] = a[k]-a[z] 임을 이용
import bisect
a = []
n = int(input())
for _ in range(n):
    a.append(int(input()))

a2 = set() # 두수의 합을 미리 구해두기
for x in a:
    for y in a:
        a2.add(x+y)

a.sort() # 입력 배열 정렬
flag = False
for k in range(n-1, -1, -1): # 최대값 a[k]를 찾아야 하므로 뒤에서부터 선택
    for z in range(n): # a[z] 선택
        if a[k]-a[z] in a2: # a[k]-a[z]값이 a2안에 존재하면 출력
            print(a[k])
            flag = True
            break
    if flag:
        break