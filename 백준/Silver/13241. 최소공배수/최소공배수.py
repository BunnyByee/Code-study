# 유클리드 호제법 활용
# 1. 최대공약수 먼저 구하기
def gcd(a,b):
    while b != 0 :
        a, b = b, a%b
    return a

# 2. 최소공배수 구하기
def lcm(m,n):
    return m * n // gcd(a,b)

# 3. 결과값 도출
a, b = map(int,input().split())
print(lcm(a,b))