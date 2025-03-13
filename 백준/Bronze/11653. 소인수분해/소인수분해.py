n = int(input())

while(n%2 == 0):
    print(2)
    n //= 2

i = 3
while (i * i <= n):
    while n % i == 0 :
        print(i)
        n //= i
    i += 2

if n > 1:
    print(n)