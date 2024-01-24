import sys

input = sys.stdin.readline

n = int(input())
seats = str(input())
arr = ["*"]
i = 0

while i <= n:
    if seats[i] == "S":
        arr.append(seats[i])
        arr.append("*")
    # LL이 연속으로 존재하는지 알기 위함
    elif seats[i] == "L" and seats[i + 1] == "L":
        arr.append(seats[i])
        arr.append(seats[i + 1])
        arr.append("*")
        i += 1
    i += 1

alpha_cnt = len(arr) - arr.count("*")
star_cnt = arr.count("*")

if alpha_cnt < star_cnt:
    print(alpha_cnt)
else:
    print(star_cnt)
