n, m = map(int, input().split())
girls = {}
for i in range(n):
    group = input()
    num = int(input())
    for _ in range(num):
        girls[input()] = group



for i in range(m):
    name = input()
    option = int(input())
    if option: # 이름이 주어지면 그룹 출력
        print(girls[name])
    else:
        members = []
        for k in girls.keys():
            if girls[k] == name:
                members.append(k)
        members.sort()
        print("\n".join(members))