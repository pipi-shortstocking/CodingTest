def solution(n, lost, reserve):
    answer = n - len(lost)

    # 여벌 옷이 있는 학생(여벌 옷이 있지만 도난 당할 수 있음)
    new_reserve = set(reserve) - set(lost)
    # answer += len(new_reserve) # 여벌 옷이 있으면 체육 수업 듣기 가능

    for l in lost:
        # print("lost", l)
        if l-1 in new_reserve:
            # lost.remove(l)
            new_reserve.remove(l-1)
            answer += 1
        elif l+1 in new_reserve:
            # lost.remove(l)
            new_reserve.remove(l+1)
            answer += 1
    
    return answer

# n = 5
# lost = [2,4]
# reserve = [1,3,5]
# n = 5
# lost = [2,4]
# reserve = [3]
n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))