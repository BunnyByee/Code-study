# 1. 최대공약수 구하기
# 최대공약수는 두 수중 가장 작은 수를 골라서 작은 수부터 검증 하기
def gcd(a,b) :
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0 :
            return i

# 2. 최소공배수 구하기
# 최소공배수 = a * b / 최대공약수
def lcm(a,b) :
    return a * b // gcd(a,b)

# 3. 결과값 도출
t = int(input())

for _ in range(t) :
    a, b = map(int,input().split())
    print(lcm(a,b))