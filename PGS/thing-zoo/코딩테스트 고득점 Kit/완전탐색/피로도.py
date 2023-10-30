from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for selected in permutations(range(n), n):
        now = k
        count = 0
        for i in selected:
            a, b = dungeons[i]
            if now < a: break
            now -= b
            count += 1
        answer = max(answer, count)
    return answer