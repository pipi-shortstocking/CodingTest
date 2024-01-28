import sys

input = sys.stdin.readline

string = list(input().rstrip())

alpha = "abcdefghijklmnopqrstuvwxyz"

ans = ""

for i in range(len(string)):
    # if string[i].isdigit():  # 숫자
    #     continue
    if string[i].isalpha():  # 알파벳
        if string[i].islower():  # 소문자
            idx = alpha.index(string[i]) + 13
            if idx > 25:
                idx %= 26
            string[i] = alpha[idx]
        elif string[i].isupper():  # 대문자
            ch = string[i].lower()
            idx = alpha.index(ch) + 13
            if idx > 25:
                idx %= 26
            string[i] = alpha[idx].upper()
    ans += string[i]

print(ans)
