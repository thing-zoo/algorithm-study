n = int(input())
nums = list(map(int, input().split()))
M, Y = 0, 0
for num in nums:
    Y += (num//30)+1
    M += (num//60)+1

if Y*10 < M*15:
    print('Y', Y*10)
elif Y*10 > M*15:
    print('M', M*15)
else:
    print("Y M", Y*10)