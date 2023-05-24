import sys, itertools

input = sys.stdin.readline

n = int(input())

# data = ["a", "b"]

# print(list(itertools.permutations(data, 2)))
# print(len(list(itertools.permutations(data, 2))))

data = [i for i in range(n)]
per = list(itertools.permutations(data, 2))

print(len(per))
