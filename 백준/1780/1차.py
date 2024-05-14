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
    while flag and i < side:
        if paper[i].count(check) != side:  # 모두 같은 수가 아닐 때
            flag = False
        i += 1

    if flag:
        ans[check + 1] += 1
    else:
        # 9등분
        temp = []
        if side > 2:
            for i in range(0, n, side // 3):
                for j in range(side):
                    temp.append(paper[j][i : i + side // 3])
                    if j % 3 == 2:
                        cut(temp, side // 3)
                        temp = []


cut(arr, n)
print(ans)
