import sys

input = sys.stdin.readline

n = int(input())
total = 2 * n

for i in range(1, n + 1):
    for _ in range(i - 1):
        print(" ", end="")
    for _ in range(total - (2 * i - 1)):
        print("*", end="")
    print()
for i in range(2, n + 1):
    for _ in range(int((total - (2 * i - 1)) / 2)):
        print(" ", end="")
    for _ in range(2 * i - 1):
        print("*", end="")
    print()
