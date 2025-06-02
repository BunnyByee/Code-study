from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
line = deque(map(int, input().split()))
wait = []
expected = 1

while line or wait:
    if line and line[0] == expected:
        line.popleft()
        expected += 1
    elif wait and wait[-1] == expected:
        wait.pop()
        expected += 1
    elif line:
        wait.append(line.popleft())
    else:
        break

print("Nice" if expected == n + 1 else "Sad")