# math.gcd(x,y)의 모듈을 사용하여 간단히 최대공약수를 구할 수 있음


# 유클리드 호제법
# 1) 두 수 x, y가 존재함. (x > y)
# 2) x를 y로 나눈 나머지 r을 구함
# 3) 만약 r != 0이라면, x에 y를, y에 r을 대입
# 4) r이 0이 될 때까지, 2 - 3단계 반복
# 5) r = 0일 경우, y는 최대공약수
def gcd(x, y):
    # x > y 의 조건을 만족해야 함
    while y:
        x, y = y, x % y
    return x
