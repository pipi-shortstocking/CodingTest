num = int(input())  # 색종이의 수
arr = [0] * num
width = 0

for i in range(num):
    a, b = list(map(int, input().split()))
    arr[i] = a, b
    #width += ((b+10)-b)*((a+10)-a)

    # 색종이가 겹칠 조건 생각하기
    if arr[i][i] < a or arr[i][i]+10 > a:
        # 색종이가 겹치는 부분 구하기

        #print(arr[0][0], arr[0][1])
