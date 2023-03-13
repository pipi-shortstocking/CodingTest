num = int(input())  # 색종이의 수
arr = [0] * num
width = 0

for i in range(num):
    a, b = list(map(int, input().split()))
    arr[i] = a, b
    # width += ((b+10)-b)*((a+10)-a)
print(arr)

for i in range(num):
    # print(i)

    if i == 0:
        continue

    # 색종이가 겹칠 조건 생각하기
    if arr[i-1][1] < arr[i][1] and (arr[i-1][1]+10) > arr[i][1]:
        # print('yes!')
        if arr[i-1][0] < arr[i][0] and (arr[i-1][0]+10) > arr[i][0]:
            # 색종이가 겹치는 부분 구하기
            width += ((arr[i][1]+10)-arr[i-1][1]) * \
                ((arr[i][0]+10)-arr[i-1][0])
        else:
            width += ((b+10)-b)*((a+10)-a)
    else:
        # print('no~')
        width += ((b+10)-b)*((a+10)-a)

print(width)
