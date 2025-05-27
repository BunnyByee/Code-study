n, m = map(int,input().split())

no_listen = set(input() for _ in range(n))
no_look = set(input() for _ in range(m))

# 교집합
result = sorted(no_listen & no_look)

print(len(result))
print(*result, sep='\n')