import sys
input = sys.stdin.readline

n = int(input())
stack = [int(input()) for _ in range(n)]
index = 0
arr = [1]
len = 0
ans = ['+']

for num in range(2,n+1):
    # if arr[len] == stack[index]:
    while arr[len] == stack[index]:
        index += 1
        len -= 1
        arr.pop()
        ans.append('-')
    arr.append(num)
    ans.append('+')
    len += 1

print(ans)