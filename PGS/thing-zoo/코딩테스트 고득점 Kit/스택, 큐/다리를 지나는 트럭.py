def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [ 0 ] * bridge_length
    sum = 0
    while bridge:
        sum -= bridge.pop(0)
        if truck_weights:
            if sum + truck_weights[0] <= weight:
                sum += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        answer += 1
    return answer

b = 2
w = 10
t = [7,4,5,6]
print(solution(b, w, t))
