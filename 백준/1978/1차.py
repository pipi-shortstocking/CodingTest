n = int(input())

number = list(map(int, input().split()))
result = 0

for i in range(n):
    arr = []

    for j in range(1, number[i]+1):
        if number[i] % j == 0:
            arr.append(j)
    if len(arr) == 2:
        result += 1

print(result)
