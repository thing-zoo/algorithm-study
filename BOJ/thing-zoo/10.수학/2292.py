n = int(input())
x = 1 # 방 번호
level = 1 # 방의 깊이..?
while x < n:
    x += level * 6 # 방은 6의 배수만큼 늘어난다
    level += 1
print(level)