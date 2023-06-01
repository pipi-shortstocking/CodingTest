n = int(input())
cnt = n
for i in range(2 * n - 1):
    if i < n:
        for j in range(i + 1):
            print("*", end="")
        print()
    else:
        while cnt != 0:
            cnt -= 1
            for j in range(cnt):
                print("*", end="")
            print()
