def solution(numbers, hand):
    answer = ""
    l_loc = 10
    r_loc = 12

    dir = [-3, 3, -1, 1] # 상하좌우

    for num in numbers:
        if num == 0:
            num = 11

        if num in (1, 4 ,7):
            answer += "L"
            l_loc = num
        elif num in (3, 6, 9):
            answer += "R"
            r_loc = num
        else:
            flag = ""

            for d in dir:
                if l_loc + d == num:
                    flag += "l"

                if r_loc + d == num:
                    flag = "r"

            if flag == "l":
                answer += "L"
                l_loc = num
            elif flag == "r":
                answer += "R"
                r_loc = num
            elif flag in ("lr", "rl"):
                if hand == "right":
                    answer += "R"
                    r_loc = num
                else:
                    answer += "L"
                    l_loc = num

        print("num/answer", num, answer)

    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"

print(solution(numbers, hand))