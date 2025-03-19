n = int(input())
x = 0
result = 0

for i in range(1, n+1):
    for j in str(i) :
        x += int(j)
    x += i

    if (x != n) :
        x = 0
    else :
        result = i
        break
print(result)