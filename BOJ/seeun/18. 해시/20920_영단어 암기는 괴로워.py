import sys
input = sys.stdin.readline
n, m = map(int, input().split())

words = {}
for _ in range(n):
    tmp = input().rstrip()
    if tmp in words:
        words[tmp][0] += 1 # 해시에 있으면 개수만 증가
    else:
        words[tmp] = [1, len(tmp), tmp] # [단어의 개수, 단어의 길이, 단어] 저장

lst = list(words.values())
lst.sort(key = lambda x:(-x[0], -x[1], x[2])) # 자주 나오는, 길이가 긴, 사전 순으로 빠른 순서대로 정렬

for i in range(len(lst)):
    if lst[i][1] >= m: # 길이가 m보다 길면 출력
        print(lst[i][2])