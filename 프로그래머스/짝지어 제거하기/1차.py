def solution(s):
    stack = []

    for ch in s:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()

        # print(ch)
        # print(stack)
        # print('-----')

    if not stack:
        answer = 1
    else:
        answer = 0

    return answer

# print(solution("baabaa"))
# print()
# print(solution("cdcd"))