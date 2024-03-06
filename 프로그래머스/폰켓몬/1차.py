def solution(nums):
    pick_num = int(len(nums) / 2)
    arr = [0] * 200001
    kind = 0

    for num in nums:
        if arr[num] == 0:
            kind += 1
            arr[num] += 1

    if kind > pick_num:
        return pick_num
    else:
        return kind


nums = list(map(int, input().split()))

print(solution(nums))

# nums = list(map(int, input().split()))
# arr = [0] * 200001
# kind = 0

# for num in nums:
#     if arr[num] == 0:
#         kind += 1
#         arr[num] += 1

# print(kind)
