import sys

input = sys.stdin.readline

n, m = map(int, input().split())
list_num = {}
list_name = {}

for i in range(1, n + 1):
    name = str(input().rstrip())
    list_num[i] = name
    list_name[name] = i

for j in range(m):
    ans = input().rstrip()

    if ans.isdigit():
        print(list_num[int(ans)])
    else:
        print(list_name[ans])
