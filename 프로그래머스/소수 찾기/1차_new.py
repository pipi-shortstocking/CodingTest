from itertools import permutations

def solution(numbers):
    answer = []
    arr = list(numbers)

    for i in range(1, len(arr) + 1):
        for j in permutations(arr, i):
            answer.append(int("".join(map(str, j))))

    answer = sorted(list(set(answer)))
    prime_arr = make_prime_arr(answer[-1])

    count = 0
    for num in answer:
        if prime_arr[num]:
            count += 1

    return count

def make_prime_arr(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * 2, n + 1, i):
                arr[j] = False

    return arr


numbers = "17"
# numbers = "011"

print(solution(numbers))