import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1
target = 0
# target에 가장 가까운 값을 저장하기 위한 배열(초기값은 첫번째 연산)
temp = [abs(arr[start] + arr[end]), start, end]

while start < end:
    sum = arr[start] + arr[end]

    if sum == target:
        print(arr[start], arr[end])
        break

    if abs(sum) < temp[0]:
        temp = [abs(sum), start, end]
    
    if sum < target:
        start += 1
    elif sum > target:
        end -= 1

print(arr[temp[1]], arr[temp[2]])