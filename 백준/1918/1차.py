import sys

input = sys.stdin.readline

cal = str(input().rstrip())
stack = []
ans = []  # 출력

for i in cal:
    if i.isalpha():  # 피연산자
        ans.append(i)
    else:  # 연산자
        # 스택의 마지막 연산자가 가장 우선 순위가 높음
        if len(stack) != 0 and i != "(":
            if i == ")":
                ans.append(stack.pop())
            elif stack[-1] == "*" or stack[-1] == "/":
                while len(stack) != 0:
                    ans.append(stack.pop())
        stack.append(i)
    # print("ans: ", ans)
    # print("stack: ", stack)
    # print("-----------------")

while len(stack) != 0:
    if stack[-1] != "(" or stack[-1] != ")":
        ans.append(stack.pop())

print(*ans)
