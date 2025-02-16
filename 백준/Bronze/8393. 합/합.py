import sys
input = sys.stdin.readline

hap = 0

n = int(input())

for i in range(1, n+1) :
    hap = hap + i
print(hap)