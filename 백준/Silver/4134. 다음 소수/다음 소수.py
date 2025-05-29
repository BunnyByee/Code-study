import sys
import math

input = sys.stdin.readline

# 소수 (1과 자신만 있는 수)
# 숫자 x보다 작은 수에서 나눠지면 -> 소수가 아님
# 약수는 대칭이기 때문에 x의 제곱근까지 개수 세어도 됨
def is_prime(x):
    if x < 2 :
        return False
    if x == 2 :
        return True
    if x % 2 == 0 :
        return False

    for i in range(3, int(math.sqrt(x))+1, 2): # 홀수만 검사
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if is_prime(n) :
            print(n)
            break
        n += 1