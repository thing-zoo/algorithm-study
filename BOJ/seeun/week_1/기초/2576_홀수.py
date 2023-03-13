nums = []
num_sum = 0
num_min = 999
for i in range(7):
    tmp = int(input())
    if tmp % 2 == 1:
        num_sum += tmp
        if tmp<num_min:
            num_min = tmp
if num_sum == 0:
    print(-1)
else:
    print(num_sum)
    print(num_min)