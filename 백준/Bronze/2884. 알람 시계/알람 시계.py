import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if m >= 45 :
    m = m - 45
elif h != 0 :
    h = h - 1 ; m = m + 60
    m = m - 45
elif h == 0 :
    h = 23 ; m = m + 60
    m = m - 45

print(f'{h} {m}')