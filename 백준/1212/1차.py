import sys

input = sys.stdin.readline

eight = str(input().rstrip())  # 8진수 입력

ten = int(eight, 8)  # 8진수를 10진수로 변경

two = str(bin(ten))  # 2진수

print(two[2:])
