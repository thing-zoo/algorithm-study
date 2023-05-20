import bisect
n = int(input())
a = sorted(list(map(int, input().split())))

answer = 0
flag = False # 중단 플래그
# x = y + z, z = x - y
for x in range(n): # x는 한번만 방문해야함
    for y in range(n): # 좋은수를 만족하는지 확인
        if x == y: continue
        z = bisect.bisect_left(a, a[x] - a[y])
        while z < n and a[z] == a[x] - a[y]: # 같은값이 여러개있으면
            if z != x and z != y: # 다른위치면
                answer += 1 # 카운트
                flag = True
                break # 중단
            z += 1 # 증가시켜줘야할수도있음
        if flag:
            flag = False # 다시 초기화해주고
            break # 중단
print(answer)