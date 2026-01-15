# 1차.py 성공
# 시간 복잡도를 줄인 VER

from itertools import permutations

def solution(numbers):
    num_arr = [num for num in numbers]
    number_set = set()
    cnt = 0

    for length in range(1, len(num_arr) + 1):
        for p in permutations(num_arr, length):
            number_set.add(int("".join(p)))

    for num in number_set:
        if is_primary(num):
            cnt += 1

    return cnt


def is_primary(number):
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        
    return True

# numbers = "17"
# print(solution(numbers))

# numbers = "011"
# print(solution(numbers))