a = input()
b = input()

countA = [ 0 for _ in range(26) ]
countB = [ 0 for _ in range(26) ]
for v in a:
    i = ord(v) - ord('a')
    countA[i] += 1
for v in b:
    i = ord(v) - ord('a')
    countB[i] += 1

result = 0
for i in range(26):
    result += abs(countA[i] - countB[i])
print(result)