import sys
input = sys.stdin.readline

n= int(input())
num = []

# n개 입력
for _ in range(n):
    data = int(input())
    num.append(data)

# 오름차순 후 출력
num.sort()
print(*num, sep='\n')