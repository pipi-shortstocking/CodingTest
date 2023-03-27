while True:
    # a, b, c = map(int, input().split())

    # if a == b == c == 0:
    #     break

    length = list(map(int, input().split()))

    if length.count(0) == 3:
        break
    if max(length) >= sum(length) - max(length):
        print('Invalid')
    else:
        if length[0] == length[1] == length[2]:
            print('Equilateral')
        elif length[0] == length[1] or length[1] == length[2] or length[2] == length[0]:
            print('Isosceles')
        else:
            print('Scalene')
