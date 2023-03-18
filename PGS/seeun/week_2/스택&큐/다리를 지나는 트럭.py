def time_plus(times, i):
    for t in range(i):
        times[t] += 1


def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    stack = []
    time = 0
    i = 0
    times = [0] * len(truck_weights)
    complete = 0
    while True:
        time += 1
        if times[complete]>=bridge_length:
            if len(stack)>0:
                del stack[0]
                complete+=1

        if i < len(truck_weights):        
            if len(stack) == 0:
                stack.append(truck_weights[i])
                i += 1
            elif len(stack) + 1 <= bridge_length and sum(stack) + truck_weights[i]<= weight: 
                stack.append(truck_weights[i])
                i += 1
                
        time_plus(times, i)
        
        if len(stack) == 0:
            break
    answer = time
    return answer

b = 100
w = 100
t = [10,10,10,10,10,10,10,10,10,10]
print(solution(b, w, t))