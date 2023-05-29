import sys

input = sys.stdin.readline

word = str(input().rstrip())

# print(word[:10])
n = 0

while n < len(word):
    arr = word[n : n + 10]
    print(arr)
    n += 10
