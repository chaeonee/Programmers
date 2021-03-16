import heapq

def solution(jobs):
    jobs = sorted(jobs,key=lambda x: x[0])
    jobs = [[i]+jobs[i] for i in range(len(jobs))]
    
    answer, time = [0]*(len(jobs)), 0
    q = []
    while q or jobs:
        while jobs and jobs[0][1] <= time:
            n, s, t = jobs.pop(0)
            heapq.heappush(q,(t,s,n))
            
        if not q:
            n, s, t = jobs.pop(0)
            heapq.heappush(q,(t,s,n))
            time = s
            while jobs and jobs[0][1] <= time:
                n, s, t = jobs.pop(0)
                heapq.heappush(q,(t,s,n))
            
        t, s, n = heapq.heappop(q)
        time += t
        answer[n] = time-s
        
    return sum(answer)//len(answer)
