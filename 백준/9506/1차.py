while True:
    n = int(input())
    #sum = 0

    if n == -1:
        break

    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
            #sum += i
    # if sum == n:
    if sum(arr) == n:
        #print(n, '=')
        # for i in range(len(arr)-1):
        #     #print(n, '=', arr[i], end=' + ')
        #print(n, '=', ' + '.join(str(i) for i in arr))
        print(n, ' = ', ' + '.join(str(i) for i in arr), sep='')

    else:
        print(n, 'is NOT perfect.')
