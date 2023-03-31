import heapq
def solution(jobs):
    answer = 0
    n = len(jobs)
    time = 0
    hq = []
    jobs.sort()
    while jobs or hq: # 남은 작업이 없을때까지
        if hq: # 대기중인 작업이 있다면
            job_time, request_time = heapq.heappop(hq)
        else: # 대기중인 작업이 없다면
            request_time, job_time = jobs.pop(0) # 먼저 요청된 작업
        time = max(request_time, time) + job_time # 작업하기
        while jobs and jobs[0][0] <= time: # 작업중에 요청된 작업들이면
            r, j = jobs.pop(0)
            heapq.heappush(hq, (j, r)) # 힙에 넣기
        answer += time - request_time
    return answer//n
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))