n = int(input())
data = list(set([input() for _ in range(n)]))
for i in range(len(data)):
    data[i] = [len(data[i]), data[i]]
for w in sorted(data):
    print(w[1])