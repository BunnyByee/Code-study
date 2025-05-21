import sys
input = sys.stdin.readline

n = int(input())
c1 = set(map(int, input().split()))
m = int(input())
c2 = list(map(int, input().split()))

result = []

# c1에 있는 숫자가 c2에 있으면 1, 아니면 0
for i in c2 :
    if i in c1 :
        result.append(1)
    else :
        result.append(0)

print(*result)