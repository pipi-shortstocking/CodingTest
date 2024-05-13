n = int(input())
arr = []
ans = [0, 0, 0]  # -1, 0, 1

for _ in range(n):
    arr.append(list(map(int, input().split())))


def cut(paper, side):
    # 종이가 모두 같은 수로 되었는지 확인
    check = paper[0][0]
    flag = True
    i = 0
    # temp = []
    while flag and i < n:
        if paper[i].count(check) != side:  # 모두 같은 수가 아닐 때
            flag = False
            # for j in range(0, n, side // 3):
            #     # cut(paper, side)  # 수정 (9개로 나눈 배열, 사각형 한 변의 길이)
            #     print(j, j + side // 3)
            #     print(paper[i][j : j + side // 3])
        i += 1

    if flag:
        ans[check + 1] += 1


cut(arr, n)
# print(ans)
