def solution(clothes):
    groups = {}

    for name, sort in clothes:
        if sort not in groups:
            groups[sort] = [name]
        else:
            groups[sort].append(name)

    cnt = 1

    for g in groups:
        cnt *= len(groups.get(g)) + 1

    return cnt - 1

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))