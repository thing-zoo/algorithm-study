from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

queue = deque()
# hit hot dot dog cog
def bfs(begin):
    cnt = 0
    queue.append([begin, cnt])
    while queue:
        print(queue)
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for w in words:
            flag = 0
            for i in range(len(begin)):
                if w[i] != word[i]:
                    flag += 1
                if flag>1:
                    break
            if flag == 1:
                print(word, '===', w)
                words.remove(w)
                queue.append([w, cnt+1])
    return 0
print(bfs(begin))