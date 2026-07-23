def solution(land):
    answer = 0

    # n행 4열 [n][3]
    N = len(land)

    # 1행의 모든 요소를 시작점으로 해서 값을 찾고 그 중에서 가장 큰 값 리턴
    for i in range(4):
        temp_sum = land[0][i]
        prev_index = i

        for j in range(1, N):
            sort_arr = sorted(land[j])
            max_num = sort_arr[3]

            if land[j].index(max_num) == prev_index:
                max_num = sort_arr[2]

            temp_sum += max_num
            prev_index = land[j].index(max_num)

        if temp_sum > answer:
            answer = temp_sum

    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))