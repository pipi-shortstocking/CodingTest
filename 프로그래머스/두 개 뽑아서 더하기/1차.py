def solution(numbers):
    answer = []
    length = len(numbers)

    for i in range(length - 1):
        for j in range(i + 1, length):
            # print(numbers[i], numbers[j])
            temp = numbers[i] + numbers[j]
            answer.append(temp)
    
    return sorted(list(set(answer)))

# numbers = [2,1,3,4,1]
numbers = [5,0,2,7]

print(solution(numbers))