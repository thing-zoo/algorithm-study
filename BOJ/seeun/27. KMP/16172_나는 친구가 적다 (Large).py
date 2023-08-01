s = input()
k = input()
for i in range(10):
    s = s.replace(str(i), "")
print(1 if s.find(k) != -1 else 0)