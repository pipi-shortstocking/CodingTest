import sys

input = sys.stdin.readline

while True:
    try:
        string = str(input().rstrip())
        lower, upper, num, space = 0, 0, 0, 0

        for ch in string:
            if ch.islower():
                lower += 1
            elif ch.isupper():
                upper += 1
            elif ch.isdigit():
                num += 1
            elif ch.isspace():
                space += 1

        print(lower, upper, num, space)
    except EOFError:
        break
