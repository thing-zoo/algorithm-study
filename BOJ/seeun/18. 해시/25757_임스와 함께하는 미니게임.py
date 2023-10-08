import sys
input = sys.stdin.readline

n, g = input().rstrip().split()
n = int(n)
player = {}
for _ in range(n):
    player[input().rstrip()] = True

# 신청한 플레이어 인원수 // 필요한 인원수-1
if g == "Y":
    print(len(player.keys()))
elif g == "F":
    print(len(player.keys())//2)
else:
    print(len(player.keys())//3)