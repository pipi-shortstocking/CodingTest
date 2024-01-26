import sys

input = sys.stdin.readline

n = int(input())
cal = list(input().rstrip())
num = []
stack = []

# ord(cal) 문자 -> 숫자 65 ~ 90
# chr(cal) 숫자 -> 문자

for i in range(n):
    num.append(int(input()))

for i in range(len(cal)):
    if ord(cal[i]) >= 65 and ord(cal[i]) <= 90:  # 피연산자일 경우
        # cal[i] = num[ord(cal[i]) - 65]
        stack.append(num[ord(cal[i]) - 65])
    else:  # 연산자일 경우
        b = stack.pop()
        a = stack.pop()
        if cal[i] == "+":
            stack.append(a + b)
        elif cal[i] == "-":
            stack.append(a - b)
        elif cal[i] == "*":
            stack.append(a * b)
        elif cal[i] == "/":
            stack.append(a / b)
        elif cal[i] == "%":
            stack.append(a % b)

print("{:.2f}".format(stack[0]))
