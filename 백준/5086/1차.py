while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        # print('끝')
        break

    # 첫 번째 숫자가 두 번째 숫자의 약수
    if b % a == 0:
        print('factor')

    # 첫 번째 숫자가 두 번째 숫자의 배수
    elif a % b == 0:
        print('multiple')

    # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아님
    else:
        print('neither')
