import sys

input = sys.stdin.readline

cal = str(input().rstrip())
stack = []
ans = ""  # 출력

for i in cal:
    if i.isalpha():  # 피연산자
        ans += i
    # 연산자
    elif i == "(":  # 괄호가 들어오면 단순 추가
        stack.append(i)
    elif i == ")":  # 닫힌 괄호가 들어오면 (를 만날 때까지 pop
        while stack and stack[-1] != "(":  # 스택이 비었거나 (를 만날 때까지
            ans += stack.pop()
        stack.pop()  # ( 제거
    elif i in ("*", "/"):
        # 동일 우선순위 연산자는 먼저 나오는 연산자가 우선
        while stack and stack[-1] in ("*", "/"):  # 스택의 동일 우선순위 연산자를 만날 때까지
            ans += stack.pop()
        stack.append(i)
    elif i in ("+", "-"):
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.append(i)
    # print("i: ", i)
    # print("ans: ", ans)
    # print("stack: ", stack)
    # print("-----------------")

while stack:
    ans += stack.pop()

print(ans)
