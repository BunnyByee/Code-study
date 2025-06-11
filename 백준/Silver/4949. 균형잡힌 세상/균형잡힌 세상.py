import sys

def vps(s):
    stack = []
    couple = { ')': '(', ']': '[' }

    for char in s :
        # 여는 괄호면 스택에 넣기
        if char in couple.values():
            stack.append(char)
        
        # 닫는 괄호면 짝이 맞는지 확인
        elif char in couple:
            # 스택이 비어져 있거나 짝이 맞지 않으면
            if not stack or stack[-1] != couple[char] :
                return False
            stack.pop()
    # 끝났을 때 스택이 비어 있어야 함
    return not stack

# 여러 줄 입력 한꺼번에 받기
lines = sys.stdin.read().splitlines()

for line in lines:
    if line == ".":
        break
    
    print('yes' if vps(line) else 'no')