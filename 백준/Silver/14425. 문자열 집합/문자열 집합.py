n, m= map(int, input().split())

set_n = set()
num = 0

for i in range(n) :
    set_n.add(input())

for j in range(m) :
    t = input()
    if t in set_n :
        num += 1

print(num)