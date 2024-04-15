n = int(input())
crane = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
crane.sort(reverse = True)
boxes.sort(reverse = True)

if boxes[0] > crane[0]:
    print(-1)
else:
    ans = 0
    while boxes:
        for c in crane:
            if boxes and c < boxes[-1]: # 가장 가벼운 박스 조차 크레인에 실을 수 없으면 -> 다음 크레인 확인
                continue
            for b in boxes:
                if c >= b: # 현재 크레인에 실을 수 있는 박스이면
                    boxes.remove(b) # 해당 박스 싣고 삭제
                    break
        # 각 크레인마다 확인 했으면 1분 추가
        ans += 1
    print(ans)
