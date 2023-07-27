import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
result = 0

arr.sort()  # 오름차순

# while True:
#     if len(arr) == 0:
#         break
#     low = arr[0]  # 공포도가 가장 낮은 사람

#     low_group = arr[:low]  # 공포도가 가장 낮은 사람이 속한 그룹
#     print(low_group)
#     arr = arr[low:]
#     cnt += 1

# print(cnt)
