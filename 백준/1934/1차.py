import sys, math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    div = math.gcd(a,b)
    print(int(a*b/div))