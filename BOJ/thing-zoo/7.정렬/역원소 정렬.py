# import sys
# input = sys.stdin.readline

# def reverse(number): # 숫자 뒤집는 함수
#     reversed = 0
#     while number != 0:
#         reversed = reversed * 10 + number % 10
#         number //= 10
#     return reversed

# # 입력 받기
# data = list(map(int, input().rstrip().split()))
# n = data.pop(0)
# i = n - len(data)
# while i < n:
#     data += list(map(int, input().rstrip().split()))
#     i = len(data)

# # 숫자 뒤집기
# for i in range(len(data)):
#     data[i] = reverse(data[i])

# # 정렬후 출력
# for i in sorted(data):
#     print(i)

# 천재님의 풀이..
import sys

input = sys.stdin.read

n, *arr = input().split()
for i in range(int(n)):
    arr[i] = arr[i][::-1]

ans = sorted(map(int, arr))
print(*ans, sep="\n")