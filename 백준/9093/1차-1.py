import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().split()
    for word in string:
        print(word[::-1], end=" ")
    print()
