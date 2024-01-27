import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())

ab = str(a) + str(b)
cd = str(c) + str(d)

print(int(ab) + int(cd))
