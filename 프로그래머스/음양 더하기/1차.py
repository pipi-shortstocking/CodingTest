def solution(absolutes, signs):
    length = len(absolutes)
    answer = 0

    for i in range(length):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer

# absolutes = [4,7,12]
# signs = [True, False, True]

absolutes = [1,2,3]
signs = [False, False, True]

print(solution(absolutes, signs))