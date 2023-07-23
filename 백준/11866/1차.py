import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
arr_pop = []

index = 0
cnt = 0

while arr:
    index += 1
    cnt += 1
    if index >= len(arr):
        # print("len", len(arr))
        index = 0
    # print(index, cnt)
    if cnt == k:
        # print("huh")
        arr_pop.append(str(arr[index - 1]))
        arr.pop(index - 1)
        if index > 0:
            index -= 1
        cnt = 0

# print(set(arr) - set(arr_pop))
# print(arr_pop)

print("<", ", ".join(arr_pop), ">", sep="")
