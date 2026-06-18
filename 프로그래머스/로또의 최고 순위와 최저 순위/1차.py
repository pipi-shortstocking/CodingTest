def solution(lottos, win_nums):
    answer = []

    arr = [num for num in lottos if num not in win_nums]
    match_nums_count = len(lottos) - len(arr)
    zero_count = arr.count(0)

    higher_grade = grade_counter(match_nums_count + zero_count)
    lower_grade = grade_counter(match_nums_count)
    answer = [higher_grade, lower_grade]

    return answer

def grade_counter(match_count):
    if match_count == 6:
        return 1
    elif match_count == 5:
        return 2
    elif match_count == 4:
        return 3
    elif match_count == 3:
        return 4
    elif match_count == 2:
        return 5
    else:
        return 6

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))