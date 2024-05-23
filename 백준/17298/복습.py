n = int(input())
arr = list(map(int, input().split()))

ans = [-1] * n
stk = [0]  # 인덱스 저장용
for i in range(1, n):
    while stk and arr[stk[-1]] < arr[i]:
        ans[stk.pop()] = arr[i]
    stk.append(i)

print(*ans)
