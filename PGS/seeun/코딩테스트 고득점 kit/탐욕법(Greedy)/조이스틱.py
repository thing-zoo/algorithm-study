def solution(name):
    answer = 0
    cnt = [0] * len(name)
    lr = len(name)-1 # 좌우이동 초기값: 순방향으로 직진

    for i in range(len(name)):
        cnt[i] = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i])+1) # 상하 이동으로 알파벳 만들기

        # 연속된 A의 개수 구해서 좌우 이동 최소 구하기
        ls = i
        le = i+1
        while le < len(name) and name[le] == 'A': # 연속된 A의 길이 구하기
            le += 1

        # 0 -> 연속된 A 시작점 -> 0 -> 연속된 A 끝점(역방향 이동)
        # 0 -> 연속된 A 끝점(역방향 이동) -> 0 -> 연속된 A 시작점
        # 둘 중 거리가 짧은 경우로 이동
        lr = min([lr, ls*2 + (len(name)-le), ls + 2 * (len(name)-le)])
    
    answer = sum(cnt) + lr
    return answer