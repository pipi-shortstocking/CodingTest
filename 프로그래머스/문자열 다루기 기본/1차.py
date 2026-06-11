def solution(s):
    answer = False
    
    length = len(s)
    
    if length == 4 or length == 6:
        if s.isdigit():
            answer = True
        
    return answer

print(solution("a234"))