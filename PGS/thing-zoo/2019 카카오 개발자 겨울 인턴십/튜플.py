def solution(s):
    s = s.replace('{', '').replace('}', '').split(',')
    count = {}
    for i in s:
        i = int(i)
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    answer = sorted(count, key=lambda x: -count[x])
    return answer