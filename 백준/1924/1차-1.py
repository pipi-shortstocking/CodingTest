import sys

input = sys.stdin.readline

x, y = map(int, input().split())
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

y = sum(date[: x - 1]) + y
y = y % 7

if y == 0:
    print("SUN")
elif y == 1:
    print("MON")
elif y == 2:
    print("TUE")
elif y == 3:
    print("WED")
elif y == 4:
    print("THU")
elif y == 5:
    print("FRI")
elif y == 6:
    print("SAT")
