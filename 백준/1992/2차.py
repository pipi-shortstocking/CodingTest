n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input())))


def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return -1
    return True


def solve(x, y, z):
    if check(x, y, z) == -1:  # 쪼개져야할 경우
        print("(", end="")

        n = z // 2
        for i in range(2):
            for j in range(2):
                solve(x + i * n, y + j * n, n)
        print(")", end="")

    elif arr[x][y] == 1:
        print(1, end="")

    elif arr[x][y] == 0:
        print(0, end="")


solve(0, 0, n)
