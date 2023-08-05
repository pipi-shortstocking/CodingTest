import sys
input = sys.stdin.readline

string = list(input().rstrip())
n = int(input())
cur = len(string)

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == 'L':
        if cur == 0:
            cur = 0
        else:
            cur -= 1
    elif cmd[0] == 'D':
        if cur == len(string):
            cur = len(string)
        else:
            cur += 1
    elif cmd[0] == 'B':
        if cur == 0:
            continue
        else:
            del(string[cur-1])
            cur -= 1
    elif cmd[0] == 'P':
        string.insert(cur, cmd[1])
        cur += 1

    # print(string, cur)

for i in string:
    print(i, end='')
print()