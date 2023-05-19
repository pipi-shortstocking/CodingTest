import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        div = a%b
        a = b
        b = div
    return a


a,b = map(int, input().split())

gcd_result = gcd(a,b)

print(int(a*b/gcd_result))