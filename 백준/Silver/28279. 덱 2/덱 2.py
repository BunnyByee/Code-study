from collections import deque
import sys
input = sys.stdin.readline

dq = deque()

n = int(input())

for _ in range(n):
    command = input().rstrip()

    # 1 X : front-push
    if command.startswith('1') :
        _, x = command.split()
        dq.appendleft(int(x))

    # 2 X : back-push
    elif command.startswith('2'):
        _, x = command.split()
        dq.append(int(x))
    
    # 3 : front-pop
    elif command == '3' :
        print(dq.popleft() if dq else -1)
    
    # 4 : back-pop
    elif command == '4' :
        print(dq.pop() if dq else -1)
    
    # 5 : size
    elif command == '5' :
        print(len(dq))

    # 6 : empty
    elif command == '6' :
        print(0 if dq else 1)
    
    # 7 : front
    elif command == '7':
        print(dq[0] if dq else -1)

    # 8 : back
    elif command == '8':
        print(dq[-1] if dq else -1)