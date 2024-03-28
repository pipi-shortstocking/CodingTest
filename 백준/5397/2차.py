import sys

input = sys.stdin.readline

n = int(input())  # 테스트 개수

for _ in range(n):
    string = str(input().rstrip())
    arr1 = []
    arr2 = []

    for ch in string:
        if ch == "<" and arr1:
            arr2.append(arr1.pop())
        elif ch == ">" and arr2:
            arr1.append(arr2.pop())
        elif ch == "-" and arr1:
            arr1.pop()
        elif ch.isalpha() or ch.isdigit():  # 대소문자, 숫자
            arr1.append(ch)

    arr2.reverse()
    ans = arr1 + arr2
    print("".join(ans))
