import sys

input = sys.stdin.readline

n = int(input())
cnt = 1
stk = []
ans = []

for i in range(n):
    num = int(input())

    while cnt <= num:
        stk.append(cnt)
        ans.append("+")
        cnt += 1

    if stk[-1] == num:
        stk.pop()
        ans.append("-")

if stk:
    print("NO")
else:
    for i in ans:
        print(i)
