s = input()
words = [s[i:] for i in range(len(s))]
for i in sorted(words):
    print(i)