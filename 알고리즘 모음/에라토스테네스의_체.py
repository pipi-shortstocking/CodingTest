# 여러 개의 수가 소수가 아닌지 판별할 때 사용
# N보다 작거나 같은 모든 소수를 찾을 때 사용

# n개의 배열의 각 인덱스 값에 해당하는 수의 소수 여부 저장

import math

n = 1000000
arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

## fast ver.
n = 1000000
arr = [True] * (n + 1)

for i in range(2, int(n**0.5) + 1):
    if arr[i]:
        for j in range(i * 2, n, i):
            if arr[i]:
                arr[j] = False
