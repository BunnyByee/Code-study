import sys
# 개행 추가됨
input = sys.stdin.readline

n, m = map(int,input().split())

no_listen = set(input().strip() for _ in range(n))
no_look = set(input().strip() for _ in range(m))

# 교집합
result = sorted(no_listen & no_look)

print(len(result))
print(*result, sep='\n')