import sys

input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        tmp = a%b
        a = b
        b = tmp
    return a

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

d = d1*d2
n = n1 * d2 + n2 * d1

d = int(d/gcd(d,n))
n = int(n/gcd(d,n))

print(n,d)