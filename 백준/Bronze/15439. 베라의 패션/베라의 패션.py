import sys

n = int(sys.stdin.readline())

# 서로 다른 색상 조합 개수 : n * (n-1)
print(n*(n-1))