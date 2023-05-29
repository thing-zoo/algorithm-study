from collections import defaultdict
s = input()
partition = defaultdict(int)
for i in range(1, len(s)+1): # 몇글자짜리 만들지
    for j in range(0, len(s)-i+1): # 어디서부터 만들지
        partition[s[j:j+i]] += 1

print(len(partition.keys())) # 키의 개수 출력