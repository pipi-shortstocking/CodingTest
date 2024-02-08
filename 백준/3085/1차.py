import sys

input = sys.stdin.readline

n = int(input())

arr = [list(input().rstrip()) for _ in range(n)]

result = 0


# 가로 확인
def check_col():
    global result  # 전역 변수

    for k in range(n):
        len = 1
        for l in range(n - 1):
            if arr[k][l] == arr[k][l + 1]:
                len += 1
                result = max(result, len)
            else:
                len = 1


# 세로 확인
def check_row():
    global result

    for k in range(n):
        len = 1
        for l in range(n - 1):
            if arr[l][k] == arr[l + 1][k]:
                len += 1
                result = max(result, len)
            else:
                len = 1


for i in range(n):
    for j in range(n - 1):
        # 우 확인
        if arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            check_col()  # 가로 확인
            check_row()  # 세로 확인
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]  # 원위치
        # 하 확인
        if arr[j][i] != arr[j + 1][i]:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            check_col()
            check_row()
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]

print(result)
