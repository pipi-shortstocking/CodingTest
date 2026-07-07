from itertools import permutations

def solution(k, dungeons):
    # 던전 탐색 순서 리스트 만들기
    d_length = len(dungeons)
    d_index = [i for i in range(d_length)]
    d_search = [] # 던전 탐색 순서 리스트
    for order in permutations(d_index, d_length):
        d_search.append(list(order))

    max_count = 0
    for order in d_search: # [0,1,2]
        count = 0

        hp = dungeons[order[0]][0]
        for d in order: # 0, 1 ,2
            value = dungeons[d][1]

            # print("확인: ", hp, value, count)

            if hp < value:
                break

            hp = hp - value
            count += 1

        if count > max_count:
            max_count = count  

        # print(max_count, count)

    return max_count

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))