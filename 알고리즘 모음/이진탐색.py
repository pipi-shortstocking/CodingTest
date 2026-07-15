# 배열에서 특정 값을 찾을 때
arr = []
target = 0

def binary():
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

# 조건을 만족하는 최솟값/최댓값
# 최솟값일 경우
if 조건 만족:
    right = mid - 1 # 더 줄여보기
else:
    left = mid + 1

return left