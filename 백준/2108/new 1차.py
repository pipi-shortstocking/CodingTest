import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a = int(input())
    arr.append(a)

#산술평균
avg = sum(arr)/len(arr)
print(round(avg))

#중앙값
sorted_arr = sorted(arr)
index = len(arr)//2
print(sorted_arr[index])

#최빈값 - 많이 나온 값(여러 개일 경우 최빈값 중 두번째로 작은 값)
dict_arr = dict(Counter(sorted_arr))
dict_sorted = sorted(dict_arr.items(), key=lambda x: x[1], reverse=True)

if n > 1 and dict_sorted[0][1] == dict_sorted[1][1]:
    print(dict_sorted[1][0])
else:
    print(dict_sorted[0][0])

#범위
range = sorted_arr[n-1] - sorted_arr[0]
print(range)