n = int(input())

working = set()

for i in range(n) :
    name, log = input().split()
    if log == 'enter' :
        working.add(name)
    else :
        working.discard(name)

for name in sorted(working, reverse=True):
    print(name)