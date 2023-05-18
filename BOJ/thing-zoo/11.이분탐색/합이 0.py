# 시도1) 맞는것 같다만 파이썬에서는 시간초과...
# x + y + z = 0, z = -(x + y)
# import bisect
# n = int(input())
# a = sorted(list(map(int, input().split())))
# answer = 0
# for x in range(n-1):
#     for y in range(x+1, n):    
#         lower = bisect.bisect_left(a[y+1:], -(a[x]+a[y])) # 중복을 피하기 위해 y 이후에서 z 골라야함
#         upper = bisect.bisect_right(a[y+1:], -(a[x]+a[y]))
#         answer += upper - lower # z의 개수 카운트
# print(answer)

# 시도2) 투포인터 접근
import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
answer = 0
for x in range(n-2):
    y = x + 1
    z = n - 1
    while y < z:
        total = a[x] + a[y] + a[z]
        if total == 0: # -4 1 2 2
            if a[y] == a[z]:
                answer += z - y
            else:
                answer += z - bisect.bisect_left(a, a[z]) + 1
            y += 1
        elif total > 0:
            z -= 1
        else:
            y += 1
print(answer)