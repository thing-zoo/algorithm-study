n, game = input().split()
player = [input() for _ in range(int(n))]
player = list(set(player))

if game == 'Y': # 윷놀이
    print(len(player))
elif game == 'F': # 같은그림 찾기
    print(len(player)//2)
else: # 원카드
    print(len(player)//3)