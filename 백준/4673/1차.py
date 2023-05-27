arr = [num for num in range(1, 10001)]
for i in range(1, 10001):
    str_i = str(i)
    cnt = i
    for j in range(len(str_i)):
        cnt += int(str_i[j])
    if cnt in arr:
        arr.remove(cnt)

for i in range(len(arr)):
    print(arr[i])
