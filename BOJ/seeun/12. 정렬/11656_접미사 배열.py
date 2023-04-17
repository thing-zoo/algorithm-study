s = input()
slist = []
for i in range(len(s)):
    slist.append(s[i:])
slist.sort()
print("\n".join(slist))