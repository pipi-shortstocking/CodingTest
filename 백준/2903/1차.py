import sys
input = sys.stdin.readline

n = int(input())
dot = 4
add = 0
sub = 0

if n == 0:
    print(dot)
else:
    for i in range(n):
        add += 5*(4**i)
    for j in range(1, n+1):
        sub += ((2**j)-1)//2*(2**j)

    total = dot + add - sub

    print(total)
