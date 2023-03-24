#arr = []

arr1 = []
arr2 = []

for i in range(3):
    x, y = map(int, input().split())
    #arr.append((x, y))
    arr1.append(x)
    arr2.append(y)

for i in range(3):
    if arr1.count(arr1[i]) == 1:
        missing_x = arr1[i]
    if arr2.count(arr2[i]) == 1:
        missing_y = arr2[i]

print(missing_x, missing_y)

# num1 = []
# num2=[]
# for i in range(3):
#     #print(arr[i][0])
#     # print(arr[i].count(arr[i][0]))
#     num1.append(arr[i][0])
#     num2.append(arr[i][1])


# print(arr)
