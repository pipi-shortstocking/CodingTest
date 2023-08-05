import sys
input = sys.stdin.readline

arr1 = list(input().rstrip())
n = int(input())
arr2 = []


# 커서를 기준으로 1,2를 나눔
for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'L' and arr1:
        arr2.append(arr1.pop())
    elif cmd[0] == 'D' and arr2:
        arr1.append(arr2.pop())
    elif cmd[0] == 'B' and arr1:
        arr1.pop()
    elif cmd[0] == 'P':
        arr1.append(cmd[1])

arr = arr1 + list(reversed(arr2))
print("".join(arr))