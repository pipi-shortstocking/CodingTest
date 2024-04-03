import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    stk = []

    word = str(input().rstrip())
    for ch in word:
        if len(stk) == 0:
            stk.append(ch)
        else:
            if ch == stk[-1]:
                stk.pop()
            else:
                stk.append(ch)
    
    if len(stk) == 0:
        cnt += 1

print(cnt)
