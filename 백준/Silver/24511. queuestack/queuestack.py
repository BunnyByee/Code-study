from collections import deque
import sys
input = sys.stdin.readline

# 자료형 개수
n = int(input())
a = list(map(int, input().split()))
b = input().split()

# 삽입할 원소 개수
m = int(input())
c = input().split()

queue = deque([])
result = []

for i in range(n):
    if a[i] == 0:
        queue.append(b[i])

for i in range(m):
    queue.appendleft(c[i])
    result.append(queue.pop())

print(*result)