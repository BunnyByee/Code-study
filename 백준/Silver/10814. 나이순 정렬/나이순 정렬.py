import sys
input = sys.stdin.readline

n = int(input())
member = []

for _ in range(n):
    num, word = input().split()
    num = int(num)
    data = (num, word)
    member.append(data)

member.sort(key=lambda x: x[0])

for m in member:
    print(m[0], m[1])