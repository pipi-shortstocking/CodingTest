def setting(data):
    return data[1]


n = int(input())

arr = []

for i in range(n):
    name, score = map(str, input().split())
    arr.append((name, int(score)))
    # input_data = input().split()
    # arr.append((input_data[0], int(input_data[1])))

arr = sorted(arr, key=setting)
# arr = sorted(arr, key=lambda student: student[1])

for i in range(n):
    print(arr[i][0], end=" ")

# for student in arr:
#     print(student[0], end=" ")
