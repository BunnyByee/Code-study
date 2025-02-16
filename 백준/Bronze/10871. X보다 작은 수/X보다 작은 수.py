b = []

n, x = map(int, input().split())
a = input().split()

for i in range(n) :
    if int(a[i]) < x :
        b.append(a[i])

for j in b :
    print(j, end=" ")