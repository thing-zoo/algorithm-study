# 내 코드
# import math
# n = int(input())
# count = 0
# for i in str(math.factorial(n))[::-1]:
#     if i == "0":
#         count += 1
#     else:
#         break
# print(count)

# 다른 코드(더 효율적인듯)
n = int(input())
print(n//5 + n//25 + n//125)