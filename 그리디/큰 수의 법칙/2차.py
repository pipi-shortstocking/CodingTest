N, M, K = map(int, input().split())
data = list(map(int, input().split()))

result = 0
data.sort()
first = data[N-1]
second = data[N-2]

while True:
    for i in range(K):
        if M == 0:
            break  # 1차에서 작성하지 않아 문제가 되었음
        result += first
        M -= 1  # 1차에서 count를 선언하여 작성하였던 부분을 이미 선언되어있는 M으로 변경
        print("f :", result)

    if M == 0:
        break

    result += second
    M -= 1
    print("d:", result)

print(result)
