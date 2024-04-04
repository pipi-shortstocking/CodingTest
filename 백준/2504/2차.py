import sys

input = sys.stdin.readline

arr = str(input().rstrip())
stk = []
sum, num = 0, 1

for i in range(len(arr)):
    if arr[i] == "(":
        stk.append(arr[i])
        num *= 2
    elif arr[i] == "[":
        stk.append(arr[i])
        num *= 3
    elif arr[i] == ")":
        if not stk or stk[-1] != "(":
            sum = 0
            break
        if arr[i - 1] == "(":
            sum += num
        num /= 2
        stk.pop()
    else:
        if not stk or stk[-1] != "[":
            sum = 0
            break
        if arr[i - 1] == "[":
            sum += num
        num /= 3
        stk.pop()

print(int(sum))
