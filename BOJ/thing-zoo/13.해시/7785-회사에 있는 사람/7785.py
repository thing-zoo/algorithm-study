s = set()
for _ in range(int(input())):
    name, info = input().split()
    if info == "enter": s.add(name)
    else: s.remove(name)
for name in sorted(s, reverse=True):
    print(name)