from collections import defaultdict
s = input()
d = defaultdict(int)
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        d[s[i:j]] += 1
print(len(d))