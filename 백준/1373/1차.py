import sys

input = sys.stdin.readline

two = str(input().rstrip())  # 2진수 입력

ten = int(two, 2)  # 2진수를 10진수로 변환

eight = str(oct(ten))  # 8진수

print(eight[2:])
