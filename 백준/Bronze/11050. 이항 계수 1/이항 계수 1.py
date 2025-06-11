n, k = map(int, input().split())

def factorial(n):
    if n <= 1 :
        return 1
    return n * factorial(n-1)

# 이항 계수 nCk => n! / (n-k)! / k!
result = factorial(n) // factorial(n-k) // factorial(k)

print(result)