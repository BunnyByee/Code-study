# 에라토스테네스의 체 응용
n, m = map(int,input().split())

is_prime = [True] * (m+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(m**0.5) + 1):
    if is_prime[i]: # True로 처리되어 있는 값이라면?
        for j in range(i*i, m+1, i): # 2의 배수, ... n의 배수
            is_prime[j] = False

for i in range(n, m+1):
    if is_prime[i]:
        print(i)