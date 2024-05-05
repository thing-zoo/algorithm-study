n = int(input())
nums = list(map(int, input().split()))
inc = [1] * n
dec = [1] * n

for i in range(1, n):
    if nums[i-1] < nums[i]:
        inc[i] = inc[i-1] + 1
        dec[i] = 1
    elif nums[i-1] > nums[i]:
        dec[i] = dec[i-1] + 1
        inc[i] = 1
    else:
        inc[i] = inc[i-1] + 1
        dec[i] = dec[i-1] + 1

print(max(max(inc), max(dec)))