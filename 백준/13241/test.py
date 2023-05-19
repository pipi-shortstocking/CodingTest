import sys,math
input = sys.stdin.readline

a,b = map(int, input().split())

gcd = math.gcd(a,b)

print(int(a*b/gcd))