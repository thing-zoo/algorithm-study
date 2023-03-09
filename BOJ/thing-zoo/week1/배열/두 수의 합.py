import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

# try1
# count = 0
# for i in data:
#     key = x - i
#     if data.count(key):
#         count += 1
# print(count//2)

# try2
data.sort()
count = 0
start = 0; end = n-1;
while start != end:
    if data[start] + data[end] == x:
        end -= 1
        count += 1
    elif data[start] + data[end] < x:
        start += 1
    else:
        end -= 1
print(count)

