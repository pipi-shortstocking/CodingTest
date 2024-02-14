import sys

input = sys.stdin.readline

n, b = map(int, input().split())

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""

while n > 0:
    ans += arr[n % b]
    n = n // b

print(ans[::-1])
