n= int(input())
num = []

# n개 입력
for _ in range(n):
    data = int(input())
    num.append(data)

# 오름차순
num.sort()

for r in num:
    print(r)