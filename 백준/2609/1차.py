import sys,math
input = sys.stdin.readline

a,b = map(int, input().split())

GCD = math.gcd(a,b)
LCM = int(a*b/GCD)

print(GCD)
print(LCM)