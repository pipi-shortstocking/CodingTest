def solution(numbers, target):
    def dfs( index, current_sum):
        # 종료 조건: 모든 숫자를 다 선택했을 때
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    return dfs(0, 0)
    

numbers = [1, 1, 1, 1, 1]
target = 3

# numbers = [4, 1, 2, 1]
# target = 4

print(solution(numbers, target))