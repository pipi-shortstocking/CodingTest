import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    g = 0

    for i in range(1, n+1):
        g += i * (n//i)
    
    print(g)