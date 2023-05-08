import sys
from itertools import combinations

input = sys.stdin.readline

string = str(input().rstrip())
arr = []

# arr = [i for i in string]
# print(list(set(arr)))

# arr = []
# for i in range(1, len(string)):
#     arr.append((string[i - 1], string[i]))
# print(arr)

# arr = []
# for i in range(2, len(string)):
#     arr.append((string[i - 2], string[i - 1], string[i]))
# print(set(arr))

# arr = []
# for i in range(3, len(string)):
#     arr.append((string[i - 3], string[i - 2], string[i - 1], string[i]))
# print(arr)

for i in range(len(string)):
    for j in range(i, len(string)):
        arr.append(string[i : j + 1])

print(len(set(arr)))
