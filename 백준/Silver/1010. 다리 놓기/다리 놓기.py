import sys
input = sys.stdin.readline

def factorial(n):
    if n <= 1 :
        return 1
    return n * factorial(n-1)

# 이항 계수 nCk => n! / (n-k)! / k!
def nCk(n,k):
    return factorial(n) // factorial(n-k) // factorial(k)

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    print(nCk(m,n))