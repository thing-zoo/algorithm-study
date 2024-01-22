import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
words = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m: continue
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
result = []
for word, count in words.items():
    result.append((-count, -len(word), word))
result.sort()
for _, _, word in result:
    print(word)