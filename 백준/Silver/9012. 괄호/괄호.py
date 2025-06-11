import sys
input = sys.stdin.readline

def vps(s):
    stack = []
    for char in s :
        if char == '(' :
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0 # 스택이 비어있으면 성공

n = int(input())

for _ in range(n):
    s = input()
    if vps(s) :
        print("YES")
    else :
        print("NO")