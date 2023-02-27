n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for a in range(m):
    i, j, k = map(int, input().split())
    m_e = arr[k-1:j]  # mid부터 end까지
    # print(m_e)
    z_b = arr[0:i-1]  # 0부터 begin까지
    # print(z_b)
    e_n = arr[j:n]  # end부터 n까지
    # print(e_n)
    b_m = arr[i-1:k-1]  # begin부터 mid까지
    # print(b_m)
    arr = z_b+m_e+b_m+e_n

for b in range(len(arr)):
    print(arr[b], end=' ')
