import sys
input = sys.stdin.readline

T = int(input())

btns = [300, 60, 10]
cnt = []

for btn in btns:
    cnt.append(T//btn)
    T = T % btn
    
if T != 0:
    print(-1)
else:
    print(*cnt)