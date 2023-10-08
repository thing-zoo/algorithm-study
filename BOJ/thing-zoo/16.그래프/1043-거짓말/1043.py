n, m = map(int, input().split()) # n: 사람 수, m: 파티 수
know = set(input().split()[1:]) # 진실을 아는 사람 수[0], 번호들[1:]

parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & know: # 파티에 진실을 아는 회원이 있으면
            know = know.union(party) # 그 파티원 모두 진실을 알게 됨

cnt = 0
for party in parties:
    if party & know:
        continue
    cnt += 1

print(cnt)