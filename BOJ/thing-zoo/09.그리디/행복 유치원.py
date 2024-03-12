n, k = map(int, input().split())
heights = list(map(int, input().split())) # 오름차순으로 입력됨
diff = [heights[i+1]-heights[i] for i in range(n-1)] # 인접 키 간 차이 구하기
diff.sort() # 오름차순 정렬
# k조로 나누려면, n-1개의 차중에서 k-1개의 차를 빼고 선택하면됨
# n-1-(k-1) = n-k개의 차를 선택하면 됨
print(sum(diff[:n-k]))