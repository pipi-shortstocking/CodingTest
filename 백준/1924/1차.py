import sys

input = sys.stdin.readline

x, y = map(int, input().split())

# 1월 / 10월
if x == 1 or x == 10:
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
# 2월/ 3월 / 11월
if x == 2 or x == 3 or x == 11:
    y = y % 7
    if y == 0:
        print("WED")
    elif y == 1:
        print("THU")
    elif y == 2:
        print("FRI")
    elif y == 3:
        print("SAT")
    elif y == 4:
        print("SUN")
    elif y == 5:
        print("MON")
    elif y == 6:
        print("TUE")
# 4월 / 7월
if x == 4 or x == 7:
    y = y % 7
    if y == 0:
        print("SAT")
    elif y == 1:
        print("SUN")
    elif y == 2:
        print("MON")
    elif y == 3:
        print("TUE")
    elif y == 4:
        print("WED")
    elif y == 5:
        print("THU")
    elif y == 6:
        print("FRI")
# 5월
if x == 5:
    y = y % 7
    if y == 0:
        print("MON")
    elif y == 1:
        print("TUE")
    elif y == 2:
        print("WED")
    elif y == 3:
        print("THU")
    elif y == 4:
        print("FRI")
    elif y == 5:
        print("SAT")
    elif y == 6:
        print("SUN")
# 6월
if x == 6:
    y = y % 7
    if y == 0:
        print("THU")
    elif y == 1:
        print("FRI")
    elif y == 2:
        print("SAT")
    elif y == 3:
        print("SUN")
    elif y == 4:
        print("MON")
    elif y == 5:
        print("TUE")
    elif y == 6:
        print("WED")
# 8월
if x == 8:
    y = y % 7
    if y == 0:
        print("TUE")
    elif y == 1:
        print("WED")
    elif y == 2:
        print("THU")
    elif y == 3:
        print("FRI")
    elif y == 4:
        print("SAT")
    elif y == 5:
        print("SUN")
    elif y == 6:
        print("MON")
# 9월 / 12월
if x == 9 or x == 12:
    y = y % 7
    if y == 0:
        print("FRI")
    elif y == 1:
        print("SAT")
    elif y == 2:
        print("SUN")
    elif y == 3:
        print("MON")
    elif y == 4:
        print("TUE")
    elif y == 5:
        print("WED")
    elif y == 6:
        print("THU")
