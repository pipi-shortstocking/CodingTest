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
    if p.count("(") != p.count(")"):
        return False

    return True

# 균형 잡힌 문자열 만들기
def find_balance(p):
    left, right = 0, 0
    for i, c in enumerate(p):
        if c == "(":
            left += 1
        else:
            right += 1

        if left == right:
            return i + 1

# 변환
def trans(p):
    if len(p) == 0:
        return ""

    balance_point = find_balance(p)
    
    u = p[:balance_point] # 이미 균현잡힌 문자열로 검증되어 나옴
    v = p[balance_point:]

    if is_right(u):
        return u + trans(v)
    else:
        temp = "(" + trans(v) + ")" # 4-3 단계
        u = u[1:len(u)-1]
        new_u = ""

        for j in u:
            if j == "(":
                new_u += ")"
            else:
                new_u += "("

        return temp + new_u

# p = "(()())()"
p = ")("
# p = "()))((()"

print(solution(p))