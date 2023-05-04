import sys
import operator
input = sys.stdin.readline

arr = {}
n = int(input())

for i in range(n):
    age, name = map(str, input().rstrip().split())
    age_int = int(age)
    arr[name] = age_int

arr_sort = sorted(arr.items(), key=operator. itemgetter(1))

for key, value in arr_sort:
    print(value, key)
