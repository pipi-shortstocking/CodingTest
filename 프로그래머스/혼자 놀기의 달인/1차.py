def solution(cards):
    # 인덱스 + 1로 계산해야 함
    length = len(cards) + 1
    visited = [False] * length
    cnt_arr = []

    # visited를 순회하다가 False를 발견하면 탐색 함수 실행
    for i in range(1, length):
        count = 0

        if not visited[i]:
            index = i
            while not visited[index]:
                visited[index] = True
                index = cards[index - 1]
                count += 1

        cnt_arr.append(count)

    cnt_arr.sort(reverse=True)

    if cnt_arr[1] == 0:
        return 0
    else:
        return cnt_arr[0] * cnt_arr[1]

cards = [8,6,3,7,2,5,1,4]
print(solution(cards))