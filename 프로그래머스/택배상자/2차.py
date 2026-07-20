def solution(order):
    box_count = len(order)
    extra_container = []
    truck_count = 0
    box = 1

    while box != box_count + 1:
        if box == order[0]:
            truck_count += 1
            order.pop(0)
            box += 1
        elif len(extra_container) != 0 and extra_container[-1] == order[0]:
            truck_count += 1
            order.pop(0)
            extra_container.pop()
        else:
            extra_container.append(box)
            box += 1

    if len(extra_container) != 0:
        while len(extra_container) != 0:
            if extra_container[-1] == order[0]:
                truck_count += 1
                order.pop(0)
                extra_container.pop()
            else:
                break

    return truck_count


# order = [4, 3, 1, 2, 5] # 2
# order = [5, 4, 3, 2, 1] # 5
order = [3, 2, 1, 4, 5] # 5
print(solution(order))