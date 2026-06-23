def solution(s):
    stk = []
    str = list(s)

    for s in str:
        if s == "(":
            stk.append(s)
        elif s == ")":
            if stk:
                stk.pop()
            else:
                return False

    if not stk:
        return True
    else:
        return False

s = "()()"
# s = "(())()"
# s = ")()("
# s = "(()("

print(solution(s))