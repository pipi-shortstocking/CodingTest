m = int(input())
n = int(input())

num = []

# m부터 n까지 숫자 돌리기
for i in range(m, n+1):
    arr = []
    # 입력된 m값(i)에 대해 소수 여부 판단하기
    for j in range(1, i+1):
        if i % j == 0:
            arr.append(i)
    if len(arr) == 2:
        num.append(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(num[0])
