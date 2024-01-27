import sys

input = sys.stdin.readline

while True:
    string = str(input().rstrip("\n"))  # 개행문자 없애기
    lower, upper, num, space = 0, 0, 0, 0

    if not string:  # 문자가 들어오지 않으면 종료
        break

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
