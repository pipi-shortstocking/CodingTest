import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

num_list = []

for i in range(1, len(arr) + 1):
    data = list(combinations(arr, i))
    # print(data)
    for i in range(len(data)):
        num_list.append(sum(data[i]))

# print(set(num_list))
# print(min(set(num_list)))
num_list = list(set(num_list))

if min(num_list) > 1:
    print(1)
elif len(num_list) == max(num_list):
    print(max(num_list) + 1)
else:
    for i in range(max(num_list)):
        if (i + 1) != num_list[i]:
            print(i + 1)
            break
