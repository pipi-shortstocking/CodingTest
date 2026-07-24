def solution(p):
    # 올바른 괄호 문자열이므로 반환
    if is_right(p):
        return p

    # 초기 p는 '(' 와 ')'의 개수가 무조건 일치 -> '올바른'이 아니면 무조건 '균형'
    return trans(p)

# 올바른
def is_right(p):
    stack = []

    for i in p:
        if i == "(":
            stack.append(i)
        elif len(stack) != 0:
            stack.pop()

    if len(stack) != 0:
        return False

    return True

# 균형
def is_balance(p):
    if is_right(p):
        return False

    if p.count("(") != p.count(")"):
        return False

    return True

# 변환
def trans(p):
    if len(p) == 0:
        return ""

    for i in range(2, len(p)):
        u = p[:i]

        if is_balance(u):
            v = p[i:]

            if is_right(u):
                return u + trans(v)
            else:
                temp = "("
                temp = temp + trans(v) + ")" # 4-3 단계
                u = u[1:len(u)-1]
                new_u = ""

                for j in u:
                    if j == "(":
                        new_u += ")"
                    else:
                        new_u += "("

                return new_u

# p = "(()())()"
p = ")("
# p = "()))((()"

print(solution(p))