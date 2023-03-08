arr = [[0]*9 for _ in range(9)]
arr_max = []

for i in range(9):
    arr[i] = list(map(int, input().split()))
    arr_max.append(max(arr[i]))

max_num = max(arr_max)
print(max_num)

new_list = [(i+1, j+1) for i in range(9)
            for j in range(9) if arr[i][j] == max_num]

print(new_list[0][0], new_list[0][1])
