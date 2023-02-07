n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k  # n이 k로 나눠떨어지는 가장 가까운 수
    result += (n-target)  # 원래 값에서 -1의 연산을 진행할 횟수
    n = target

    if n < k:
        break

    # 11,12줄은 본래의 연산
    result += 1
    n //= k

result += (n-1)  # break에서 넘어온 n에 대해 -1의 연산을 진행할 횟수
print(result)
