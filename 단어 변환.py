from collections import deque
def solution(begin, target, words):
    q = deque([[begin, 0]]) # 단어, 거리
    n = len(target)         # 단어의 크기
    while q:
        now, d = q.popleft()
        if now == target: # 목표 단어면 종료
            return d
        for word in words: # 남은 단어중에서
            count = 0
            for i in range(n):
                if now[i] != word[i]: # 현재단어와 다른 알파벳
                    count += 1 # 개수 세기
            if count == 1: # 하나만 다르다면
                q.append([word, d+1]) # 큐에 삽입
                words.remove(word) # 단어에서 삭제
    return 0
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))