n = int(input())
arr = list(map(int, input().split()))[::-1]
temp = []
cur = 1
while arr:
    if cur == arr[-1]:
        arr.pop()
        cur += 1
    elif temp and cur == temp[-1]:
        temp.pop()
        cur += 1
    else:
        temp.append(arr.pop())
while temp and cur == temp[-1]:
    temp.pop()
    cur += 1
    
if not temp:
    print('Nice')
else:
    print('Sad')