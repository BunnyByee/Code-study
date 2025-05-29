# 기약분수 구하기 (통분 -> 덧셈 -> 약분 )
son , mom = 0, 0

# gcd, lcm 활용
def gcd(a,b):
    while b != 0 :
        a, b = b, a%b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

# 1. 통분 후 덧셈
# 분모가 최소공배수, 분자는 최소공배수로 분모를 나눈 값을 곱해야함
a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())

mom = lcm(b1, b2)
son = (mom // b1) * a1 + (mom//b2) * a2 

# 2. 기약분수로 바꾸기
# 서로소로 변환, 최대공약수로 약분
g = gcd(son, mom)
son //= g
mom //= g

print(f"{son} {mom}")