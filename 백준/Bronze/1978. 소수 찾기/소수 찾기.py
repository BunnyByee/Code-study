import math

k = int(input())
n_list = list(map(int, input().split()))

count = 0
for n in n_list :
    if (n == 1) :
            continue
    
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0 :
            break
    else :
        count += 1

print(count)