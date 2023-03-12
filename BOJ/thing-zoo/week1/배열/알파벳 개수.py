word = input()
for i in range(97,97+26):
    print(word.count(chr(i)), end=" ")