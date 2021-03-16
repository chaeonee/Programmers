import heapq

def solution(food_times, k):
    food_times = [[f,i+1] for i, f in enumerate(food_times)]
    heapq.heapify(food_times)
    #food_times = sorted(food_times, key=lambda x:x[0])
    
    turn = 0
    while food_times:
        t, n = food_times[0]
        
        if (t-turn)*len(food_times) > k:
            break
        k -= (t-turn)*len(food_times)
        turn = t
        heapq.heappop(food_times)
    
    if not food_times:
        return -1
    
    food_times = sorted(food_times, key=lambda x:x[1])
    
    return food_times[k%len(food_times)][1]
