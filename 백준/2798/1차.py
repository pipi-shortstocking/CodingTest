n, m = map(int, input().split())
card = list(map(int, input().split()))
min = 300000

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = card[i] + card[j] + card[k]  # 왜 이 방법을 생각하지 못했을까!
            if sum > m:
                continue
            elif abs(m-sum) < min:
                min = m-sum
                result = sum  # 그냥 sum을 출력하면 마지막 sum 값이 출력됨
print(result)


# for i in range(2, 4):
#     print(i)
