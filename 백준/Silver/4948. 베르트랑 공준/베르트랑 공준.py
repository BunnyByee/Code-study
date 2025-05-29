max_n = 123456*2
is_prime = [True] * (max_n+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(max_n**0.5) + 1):
    if is_prime[i]: # True로 처리되어 있는 값이라면?
        for j in range(i*i, max_n+1, i): # 2의 배수, ... n의 배수
            is_prime[j] = False

# n보다 크고, 2n보다 작거나 같은 소수의 개수 구하기

while True :
    x = int(input())

    if x == 0 :
        break
    
    cnt = 0
    for i in range(x+1, 2*x+1) :
        if is_prime[i] :
            cnt += 1
    print(cnt)