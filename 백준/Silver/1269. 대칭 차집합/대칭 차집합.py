num = 0
a, b = map(int,input().split())

s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))

# 대칭 차집합의 원소의 개수 더하기
num += len(s1 - s2)
num += len(s2 - s1)

print(num)