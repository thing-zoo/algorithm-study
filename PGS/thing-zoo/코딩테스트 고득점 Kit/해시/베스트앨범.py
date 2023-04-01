def solution(genres, plays):
    answer = []
    d = {}  # d[장르] = [(고유번호, 플레이횟수),...]
    d2 = {} # d[장르] = 총 플레이횟수
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in d:
            d[g] = [(i,p)]
        else:
            d[g].append((i,p))

        if g not in d2:
            d2[g] = p
        else:
            d2[g] += p
    for k, v in sorted(d2.items(), key=lambda x: x[1], reverse=True): # 총 플레이횟수 내림차순 정렬
        for i, p in sorted(d[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)
    return answer
genres = ["a", "b", "c", "c", "b"]
plays = [10, 3, 2, 2, 5]
print(solution(genres, plays))