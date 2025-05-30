import sys
input = sys.stdin.readline

# 에라토스테네스의 체
max_n = 1000000
is_prime = [True] * (max_n+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(max_n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, max_n+1, i):
            is_prime[j] = False

# 소수 리스트
n_list = [i for i in range(2, max_n+1) if is_prime[i]]

# 두 수의 합이 짝수 n이 되는지 개수 확인
def goldbach_count(n):
    cnt = 0
    left = 0
    right = len(n_list) - 1

    while left <= right:
        s = n_list[left] + n_list[right]
        if s == n:
            cnt += 1
            left += 1
            right -= 1
        elif s < n:
            left += 1
        else:
            right -= 1
    print(cnt)

# Result
t = int(input())

for _ in range(t) :
    a = int(input())
    goldbach_count(a)