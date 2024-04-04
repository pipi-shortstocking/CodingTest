import sys

input = sys.stdin.readline

arr = str(input().rstrip())
stk = []
append_flag, pop_flag = False, False
cal = []

for i in arr:
    if i == "(" or i == "[":
        stk.append(i)
        append_flag, pop_flag = True, False
    else:
        if (
            len(stk) == 0
            or (i == ")" and stk[-1] != "(")
            or (i == "]" and stk[-1] != "[")
        ):
            ans = 0
        else:
            if i == ")":
                if append_flag:  # 직전에 append
                    cal.append(2)
                elif pop_flag:  # 직전에 pop
                    cal  # 해결 X
            elif i == "]":
                if append_flag:  # 직전에 append
                    cal.append(3)
                elif pop_flag:  # 직전에 pop
                    cal  # 해결 X
            stk.pop()
            append_flag, pop_flag = False, True

print(ans)
