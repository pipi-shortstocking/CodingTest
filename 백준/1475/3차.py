import sys

input = sys.stdin.readline

arr = [0] * 10
room = str(input().rstrip())

for i in range(len(room)):
    num = int(room[i])
    if num == 6 or num == 9:
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[num] += 1

print(max(arr))
