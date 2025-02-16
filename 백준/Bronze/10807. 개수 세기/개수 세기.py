hap = 0

n = int(input())
a = input().split()
v = input()

for i in range(n) :
    if a[i] == v :
        hap += 1

print(hap)