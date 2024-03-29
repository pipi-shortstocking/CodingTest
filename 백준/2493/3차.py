import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))

# 초기값 
stk = [[0, tops[0]]]
ans = [0]

for i in range(1,n):
    top = [i, tops[i]]

    while stk:
        if stk[-1][1] > top[1]:
            ans.append(stk[-1][0]+1)
            break # 꼭 필요
        else:
            stk.pop()
    if not stk:
        ans.append(0)
    stk.append(top)

print(*ans)