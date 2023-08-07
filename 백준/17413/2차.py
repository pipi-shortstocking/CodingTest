import sys

input = sys.stdin.readline
sen = list(input().rstrip())

flag = False  # False는 뒤집어야 하는 상태
stack = ""
result = ""

for char in sen:
    if flag == False:
        if char == "<":
            flag = True
            stack += char
        elif char == " ":
            stack += char
            result += stack
            stack = ""
        else:
            stack = char + stack
    elif flag == True:
        stack += char
        if char == ">":
            flag = False
            result += stack
            stack = ""

print(result + stack)
