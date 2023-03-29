length = list(map(int, input().split()))

while max(length) >= sum(length)-max(length):
    a = length.index(max(length))
    length[a] -= 1

print(sum(length))
