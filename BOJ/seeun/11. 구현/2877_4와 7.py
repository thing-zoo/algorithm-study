k = int(input())
# nums = [''] * (k+3)
# for i in range(2, k+2):
#     if i % 2 == 0:
#         nums[i] = nums[i//2] + '4'
#     else:
#         nums[i] = nums[i//2] + '7'

# print(nums[k+1])

tmp = bin(k+1)[3:]
tmp = tmp.replace('0', '4')
tmp = tmp.replace('1', '7')
print(tmp)