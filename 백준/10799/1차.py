import sys

input = sys.stdin.readline

line = str(input().rstrip())
stack = []
result = 0

# 여는 괄호를 만나면 push
# 닫는 괄호를 만나면 pop
# 바로 이전에 여는 괄호가 있는 레이저라면 -> +stack 사이즈
# 파이프의 끝이라면 -> +1

for i in range(len(line)):
    if line[i] == "(":
        stack.append("(")
    elif line[i] == ")":
        stack.pop()
        if line[i - 1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)
