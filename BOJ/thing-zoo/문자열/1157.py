from collections import defaultdict
dic = defaultdict(int)
word = input()
for x in word.upper():
    dic[x] += 1
count_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
if len(count_dic) > 1 and count_dic[0][1] == count_dic[1][1]:
    print('?')
else:
    print(count_dic[0][0])