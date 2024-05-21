n = int(input())
tops = list(map(int, input().split()))

stk = [[0, tops[0]]]
arr = [0]
check = tops[0]

for i in range(1, n):
    top = [i, tops[i]]

    while stk:
        if stk[-1][1] > top[1]:
            arr.append(stk[-1][0] + 1)
            break
        else:
            stk.pop()

    if not stk:
        arr.append(0)

    stk.append(top)

print(*arr)
