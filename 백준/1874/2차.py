import sys
input = sys.stdin.readline

n = int(input())
i = 1
stack = []
ans = []

for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append(i)
        i += 1
        ans.append('+')
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        break

else:
    for i in range(len(ans)):
        print(ans[i])