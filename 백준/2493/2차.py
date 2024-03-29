import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))

# 초기값 
stk = [[0, tops[0]]]
ans = [0]

for i in range(1,n):
    top = [i, tops[i]]

    if len(stk) != 0 and top[1] < stk[-1][1]:
        ans.append(stk[-1][0]+1)
    # stk[-1]의 값이 클 때까지
    while len(stk) != 0 and top[1] > stk[-1][1]: 
        stk.pop()
        if stk: # stk이 비어있지 않을 경우
            ans.append(stk[-1][0]+1)
        else: # stk이 비어있을 경우
            ans.append(0)
    stk.append(top)

print(*ans)