t = int(input())  # 테스트 케이스의 개수

for i in range(t):
    arr = list(map(str, input().split()))  # 화성 수학식
    result = eval(arr[0])  # 첫번째 숫자 숫자 형식으로 형변환(str->int, float..)

    for j in range(len(arr)):
        if arr[j] == '@':
            result *= 3
        if arr[j] == '%':
            result += 5
        if arr[j] == '#':
            result -= 7
    print('{:.2f}'.format(result))
    #print('%0.2f' % result)
