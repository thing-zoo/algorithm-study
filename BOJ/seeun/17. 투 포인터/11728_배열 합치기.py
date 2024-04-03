import sys
input = sys.stdin.readline
alen, blen = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aidx, bidx = 0, 0
a.sort()
b.sort()
res = []
# a, b 배열에 각각 인덱스를 두고 작은 수 순서대로 통합 배열에 순서대로 넣기
# 하나의 배열이 끝났으면 나머지 배열은 그대로 통합배열에 붙이기
while True:
    if aidx < alen and bidx < blen:
        if a[aidx] < b[bidx]:
            res.append(a[aidx])
            aidx += 1
        elif a[aidx] > b[bidx]:
            res.append(b[bidx])
            bidx += 1
        else:
            res.append(a[aidx])
            res.append(b[bidx])
            aidx += 1
            bidx += 1
    elif aidx >= alen:
        res.extend(b[bidx:])
        break
    elif bidx >= blen:
        res.extend(a[aidx:])
        break

print(" ".join(map(str, res)))