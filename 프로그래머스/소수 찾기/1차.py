from itertools import permutations

def solution(numbers):
    num_arr = [num for num in numbers]
    permutations_arr = []
    primary_arr = []

    for length in range(1, len(num_arr) + 1):
        for permutation in permutations(num_arr, length):
            permutations_arr.append(int("".join(permutation)))

    for num in permutations_arr:
        if is_primary(num):
            primary_arr.append(num)

    # print("arr : ", primary_arr)
    # print("arr(set) : ", list(set(primary_arr)))
    return len(list(set(primary_arr)))

def is_primary(number): # 소수 판별 함수
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0: # 1과 자기 자신이 아닌 수로 나눠질 경우 소수가 아님
            return False
        
    return True

# numbers = "17"
# print(solution(numbers))

# numbers = "011"
# print(solution(numbers))