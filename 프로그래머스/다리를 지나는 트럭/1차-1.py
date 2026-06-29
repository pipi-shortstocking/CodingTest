from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    cnt = 0

    while truck_weights or sum(bridge) > 0:
        cnt += 1
        bridge.popleft()
        
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

        # print("초: ", cnt)
        # print("다리: ", bridge)
        # print("트럭: ", truck_weights)

    return cnt

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))