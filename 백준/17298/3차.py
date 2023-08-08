import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
stack = []
ans = [-1] * n

stack.append(0)
for i in range(1,n):
    while stack and seq[stack[-1]] < seq[i]:
        ans[stack.pop()] = seq[i]
    stack.append(i)

print(*ans)