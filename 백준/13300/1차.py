import sys

input = sys.stdin.readline

n, k = map(int, input().split())
stu = [[0, 0] for _ in range(6)]
room = 12

for _ in range(n):
    s, y = map(int, input().split())
    stu[y - 1][s] += 1

for i in range(6):
    for j in range(2):
        temp = stu[i][j]
        if temp > k:
            room -= 1
            if temp % k == 0:
                room += temp // k
            else:
                room += temp // k + 1
        elif temp == 0:
            room -= 1

print(room)
