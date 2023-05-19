import sys

input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

d = d1*d2
n = n1 * d2 + n2 * d1
gcd_result = gcd(n,d)

d = int(d/gcd_result)
n = int(n/gcd_result)

print(n,d)