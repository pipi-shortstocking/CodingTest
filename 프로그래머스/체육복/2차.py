def solution(n, lost, reserve):
    answer = n - len(lost)

    # 여벌 옷이 있는 학생(여벌 옷이 있지만 도난 당할 수 있음)
    new_reserve = set(reserve) - set(lost)
    lost.sort()
    new_reserve = sorted(new_reserve)

    for l in lost:
        if l-1 in new_reserve:
            new_reserve.remove(l-1)
            answer += 1
        elif l+1 in new_reserve:
            new_reserve.remove(l+1)
            answer += 1
    
    return answer

# n = 5
# lost = [2,4]
# reserve = [1,3,5]
# n = 5
# lost = [2,4]
# reserve = [3]
# n = 3
# lost = [3]
# reserve = [1]
n = 3
lost = [1,3]
reserve = [2] # 2
print(solution(n, lost, reserve))