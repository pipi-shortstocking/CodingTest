def solution(order):
    box_count = len(order)
    extra_container = []
    truck_count = 0

    for box in range(1, box_count + 1):
        print(box, order, extra_container)

        if box == order[0]:
            truck_count += 1
            order.pop(0)
        elif len(extra_container) != 0 and extra_container[-1] == order[0]:
            truck_count += 1
            order.pop(0)
            extra_container.pop()
        else:
            extra_container.append(box)
        
    if len(extra_container) != 0:
        while len(extra_container) != 0:
            if extra_container[-1] == order[0]:
                truck_count += 1
                order.pop(0)
                extra_container.pop()
            else:
                break

    return truck_count


# order = [4, 3, 1, 2, 5]
# order = [5, 4, 3, 2, 1]
order = [3, 2, 1, 4, 5]
print(solution(order))