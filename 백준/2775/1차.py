import sys

input = sys.stdin.readline

apt = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
for i in range(1, 15):  # 층
    floor = []
    people = 0
    for j in range(14):  # 호
        people += apt[i - 1][j]
        floor.append(people)
    apt.append(floor)

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n - 1])
