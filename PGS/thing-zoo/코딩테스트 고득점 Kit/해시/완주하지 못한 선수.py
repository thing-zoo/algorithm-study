def solution(participant, completion):
    dic_p = {}; dic_c = {}
    for p in participant:
        if p not in dic_p:
            dic_p[p] = 1
        else:
            dic_p[p] += 1
    for c in completion:
        if c not in dic_c:
            dic_c[c] = 1
        else:
            dic_c[c] += 1
    for k in dic_p:
        if k not in dic_c:
            return k
        else:
            dic_p[k] -= dic_c[k]
    for k, v in dic_p.items():
        if v == 1:
            return k
def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))