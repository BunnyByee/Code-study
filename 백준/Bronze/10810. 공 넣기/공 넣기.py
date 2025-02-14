n, m = map(int, input().split())
a = [0]*n

for i in range(m) :
    start, stop, num = map(int, input().split())
    for j in range(start-1, stop):
        a[j] = num
for s in a :
    print(s, end=" ")