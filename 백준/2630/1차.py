n = int(input())
arr = []
color = [0,0] # white, blue

for _ in range(n):
    arr.append(list(map(int,input().split())))

# 다 같은 색인지 찾는 함수
def check(x,y,n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return False
    return True

def solve(x,y,z):
    if check(x,y,z):
        color[arr[x][y]] += 1
    else:
        n = z // 2
        for i in range(2):
            for j in range(2):
                solve(x + i * n, y + j * n, n)
        

solve(0,0,n)
for c in color:
    print(c)