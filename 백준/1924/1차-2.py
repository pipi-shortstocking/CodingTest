import sys

input = sys.stdin.readline

x, y = map(int, input().split())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

y = (sum(day[: x - 1]) + y) % 7
print(date[y])
